import uuid

from django.test import TestCase
from django.conf import settings

class SupabaseConnectionTest(TestCase):
    def test_connection(self):
        try:
            # Query data dari tabel leaf_detection
            resp = settings.SUPABASE.from_("leaf_detection").select("*").limit(1).execute()
            print("Response data:", resp.data)

            # Pastikan hasil berupa list
            self.assertIsInstance(resp.data, list)
        except Exception as e:
            self.fail(f"Connection to Supabase failed: {str(e)}")

    # def test_insert(self):
    #     try:
    #         user_id = str(uuid.uuid4())

    #         data = {
    #             # "user_id": user_id,
    #             "file_name": "example_leaf.jpg",
    #             "original_url": "https://example.com/original.jpg",
    #             "detected_url": "https://example.com/detected.jpg",
    #             "prediction": {"status": "healthy"},
    #             "analysisi": {"note": "uji insert dari Django"}
    #         }

    #         resp = settings.SUPABASE.from_('leaf_detection').insert(data).execute()
    #         print('insert response:', resp)

    #         self.assertIsInstance(resp.data, list)
    #         self.assertEqual(len(resp.data), 0)

    #     except Exception as e:
    #         self.fail(f"Insert to Supabase failed: {str(e)}")