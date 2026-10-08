"""Meaningful boundary checks for catalog classifications and release claims."""
import copy
import sys
import unittest
from unittest.mock import patch
from types import SimpleNamespace
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from render_readme import activity, load, render, render_details, detail_heading, bibtex
from verify_catalog import validate_data, check_url

class ValidationTests(unittest.TestCase):
    def setUp(self):
        self.catalog = load()

    def test_catalog_is_valid(self):
        self.assertEqual(validate_data(self.catalog)[0], [])

    def test_activity_boundary_is_inclusive(self):
        base = dict(archived=False, size_kb=10, pushed_at='2026-08-09T00:00:00Z')
        self.assertEqual(activity(base, '2026-10-08'), 'active')
        base['pushed_at'] = '2026-08-08T00:00:00Z'
        self.assertEqual(activity(base, '2026-10-08'), 'reference')

    def test_archived_and_empty_are_not_active(self):
        base = dict(archived=True, size_kb=10, pushed_at='2026-10-08T00:00:00Z')
        self.assertEqual(activity(base, '2026-10-08'), 'archived')
        base.update(archived=False, size_kb=0)
        self.assertEqual(activity(base, '2026-10-08'), 'empty')

    def test_unconfirmed_code_cannot_have_url(self):
        paper = next(e for e in self.catalog['entries'] if e.get('code_status') == 'not-confirmed')
        paper['code_url'] = 'https://github.com/example/not-official'
        self.assertTrue(any('code URL/status mismatch' in e for e in validate_data(self.catalog)[0]))

    def test_empty_repository_cannot_be_project(self):
        project = next(e for e in self.catalog['entries'] if e['kind'] == 'project')
        project['github']['size_kb'] = 0
        self.assertTrue(any('empty repository cannot' in e for e in validate_data(self.catalog)[0]))

    def test_duplicate_resource_is_rejected(self):
        duplicate = copy.deepcopy(self.catalog['entries'][0]); duplicate['id'] += '-copy'
        self.catalog['entries'].append(duplicate)
        self.assertTrue(any('duplicate resource URL' in e for e in validate_data(self.catalog)[0]))

    def test_future_publication_is_rejected(self):
        self.catalog['entries'][0]['published'] = '2099-01-01'
        self.assertTrue(any('invalid/future published' in e for e in validate_data(self.catalog)[0]))

    def test_companion_artifact_requires_bilingual_label_and_url(self):
        self.catalog['entries'][0]['artifacts'] = [{'name_en': 'Data', 'url': 'not-a-url'}]
        self.assertTrue(any('incomplete companion artifact' in e for e in validate_data(self.catalog)[0]))

    def test_category_must_have_valid_major_group(self):
        self.catalog['categories'][0]['parent'] = 'missing-group'
        self.assertTrue(any('invalid parent group' in e for e in validate_data(self.catalog)[0]))

    def test_linked_work_cannot_split_across_categories(self):
        work = next(e['work_id'] for e in self.catalog['entries'] if e['kind'] == 'project')
        items = [e for e in self.catalog['entries'] if e['work_id'] == work]
        items[0]['category'] = 'surveys'
        self.assertTrue(any('inconsistent category' in e for e in validate_data(self.catalog)[0]))

    def test_tables_and_details_need_no_raw_html(self):
        for lang in ['en', 'zh']:
            result = render(self.catalog, lang)
            details = render_details(self.catalog, lang)
            self.assertNotIn('<a ', result + details)
            self.assertNotIn('阅读路线', result)
            self.assertNotIn('Reading route', result)
            for entry in self.catalog['entries']:
                self.assertEqual(details.count('## ' + detail_heading(entry) + '\n'), 1)

    def test_report_locations_require_pdf_pages(self):
        report = next(e for e in self.catalog['entries'] if e['kind'] == 'report')
        report['report_sections'][0]['pdf_pages'] = [0]
        self.assertTrue(any('invalid PDF page range' in e for e in validate_data(self.catalog)[0]))

    def test_non_arxiv_report_keeps_unknown_date(self):
        report = next(e for e in self.catalog['entries'] if e['id'] == 'report-mimo-v26')
        self.assertIsNone(report['published'])
        citation = bibtex({'entries': [report]})
        self.assertNotIn('eprint =', citation)
        self.assertNotIn('year =', citation)
        self.assertIn('first publication date unconfirmed', citation)

    def test_connection_failure_is_not_reported_as_http_404(self):
        response = SimpleNamespace(returncode=28, stdout='000\nhttps://example.org', stderr='SSL connection timeout')
        with patch('verify_catalog.subprocess.run', return_value=response) as request:
            result = check_url('https://example.org')
        self.assertIsNone(result['status'])
        self.assertEqual(result['result'], 'failed')
        self.assertIn('timeout', result['error'])
        self.assertEqual(request.call_count, 1)

    def test_head_rejection_can_recover_with_get(self):
        responses = [SimpleNamespace(returncode=0, stdout='405\nhttps://example.org', stderr=''),
                     SimpleNamespace(returncode=0, stdout='200\nhttps://example.org', stderr='')]
        with patch('verify_catalog.subprocess.run', side_effect=responses):
            result = check_url('https://example.org')
        self.assertEqual(result['result'], 'ok')
        self.assertEqual(result['method'], 'GET')
        self.assertEqual(result['status'], 200)

if __name__ == '__main__':
    unittest.main()
