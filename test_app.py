import os
import tempfile
import unittest

import app


class AppConfigTests(unittest.TestCase):
    def test_missing_ssl_cert_returns_none(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            cert_path = os.path.join(tmpdir, 'missing.pem')
            key_path = os.path.join(tmpdir, 'missing-key.pem')
            self.assertIsNone(app.get_ssl_context(cert_path=cert_path, key_path=key_path))

    def test_existing_ssl_cert_returns_tuple(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            cert_path = os.path.join(tmpdir, 'cert.pem')
            key_path = os.path.join(tmpdir, 'key.pem')
            with open(cert_path, 'w', encoding='utf-8') as cert_file:
                cert_file.write('dummy cert')
            with open(key_path, 'w', encoding='utf-8') as key_file:
                key_file.write('dummy key')

            self.assertEqual(
                app.get_ssl_context(cert_path=cert_path, key_path=key_path),
                (cert_path, key_path),
            )

    def test_prefers_localhost_cert_for_local_browser_access(self):
        original_cwd = os.getcwd()
        with tempfile.TemporaryDirectory() as tmpdir:
            try:
                os.chdir(tmpdir)
                localhost_cert = os.path.join(tmpdir, 'localhost+2.pem')
                localhost_key = os.path.join(tmpdir, 'localhost+2-key.pem')
                custom_cert = os.path.join(tmpdir, 'damclock.gd.pem')
                custom_key = os.path.join(tmpdir, 'damclock.gd-key.pem')

                for cert_path, key_path in (
                    (localhost_cert, localhost_key),
                    (custom_cert, custom_key),
                ):
                    with open(cert_path, 'w', encoding='utf-8') as cert_file:
                        cert_file.write('dummy cert')
                    with open(key_path, 'w', encoding='utf-8') as key_file:
                        key_file.write('dummy key')

                self.assertEqual(
                    app.get_ssl_context(),
                    (localhost_cert, localhost_key),
                )
            finally:
                os.chdir(original_cwd)


if __name__ == '__main__':
    unittest.main()
