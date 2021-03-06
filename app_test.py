from server import app

import unittest

class CitiesTestCase(unittest.TestCase):
  # check if the site comes up
  def test_index(self):
    tester = app.test_client(self)
    response = tester.get('/index.html', content_type='text/html')
    self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()

