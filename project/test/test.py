from project.gallery import Gallery
from unittest import TestCase, main


class GalleryTests(TestCase):
    name = 'Heaven'
    city = 'Sofia'
    meters = 1000
    open = True
    exhibitions = {}

    def setUp(self) -> None:
        self.gallery = Gallery(self.name, self.city, self.meters, self.open)

    def test_initializing(self):
        self.assertEqual(self.name, self.gallery.gallery_name)
        self.assertEqual(self.city, self.gallery.city)
        self.assertEqual(self.meters, self.gallery.area_sq_m)
        self.assertEqual(self.open, self.gallery.open_to_public)
        self.assertEqual(self.exhibitions, self.gallery.exhibitions)

    def test_gallery_name_with_invalid_data(self):
        with self.assertRaises(ValueError) as ex:
            self.gallery.gallery_name = 'Heaven/123123'
        self.assertEqual("Gallery name can contain letters and digits only!", str(ex.exception))

    def test_gallery_name_with_empty_string(self):
        with self.assertRaises(ValueError) as ex:
            self.gallery.gallery_name = " "
        self.assertEqual("Gallery name can contain letters and digits only!", str(ex.exception))

    def test_city_name_with_invalid_data_nums_and_lets(self):
        with self.assertRaises(ValueError) as ex:
            self.gallery.city = '9Heaven'
        self.assertEqual("City name must start with a letter!", str(ex.exception))

    def test_city_name_with_invalid_data_nums(self):
        with self.assertRaises(ValueError) as ex:
            self.gallery.city = '358'
        self.assertEqual("City name must start with a letter!", str(ex.exception))

    def test_city_name_with_empty_string(self):
        with self.assertRaises(ValueError) as ex:
            self.gallery.city = ' '
        self.assertEqual("City name must start with a letter!", str(ex.exception))

    def test_area_meters_with_invalid_negative_num(self):
        with self.assertRaises(ValueError) as ex:
            self.gallery.area_sq_m = -5
        self.assertEqual("Gallery area must be a positive number!", str(ex.exception))

    def test_area_meters_with_invalid_bounder_num(self):
        with self.assertRaises(ValueError) as ex:
            self.gallery.area_sq_m = 0.0
        self.assertEqual("Gallery area must be a positive number!", str(ex.exception))

    def test_add_first_new_exhibition_to_exhibitions(self):
        name = 'Heaven'
        year = 2020
        expected_result = f'Exhibition "{name}" added for the year {year}.'
        expected_result_exhibitions = {name: year}

        actual_result = self.gallery.add_exhibition(name, year)
        actual_result_exhibitions = self.gallery.exhibitions

        self.assertEqual(expected_result, actual_result)
        self.assertEqual(expected_result_exhibitions, actual_result_exhibitions)

    def test_add_exhibition_with_new_data(self):
        name = 'Heaven'
        year = 2020
        self.gallery.add_exhibition(name, year)

        name_two = 'Exhibition'
        year_two = 2022

        expected_result = f'Exhibition "{name_two}" added for the year {year_two}.'
        expected_result_exhibitions = {name: year, name_two: year_two}

        actual_result = self.gallery.add_exhibition(name_two, year_two)
        actual_result_exhibitions = self.gallery.exhibitions

        self.assertEqual(expected_result, actual_result)
        self.assertEqual(expected_result_exhibitions, actual_result_exhibitions)

    def test_try_add_exhibition_with_existing_data(self):
        name = 'Heaven'
        year = 2020
        name_two = 'Exhibition'
        year_two = 2022
        self.gallery.add_exhibition(name, year)
        self.gallery.add_exhibition(name_two, year_two)

        actual_result = self.gallery.add_exhibition(name_two, year_two)
        expected_result = f'Exhibition "{name_two}" already exists.'

        actual_result_exhibition = self.gallery.exhibitions
        expected_result_exhibition = {name: year, name_two: year_two}

        self.assertEqual(expected_result, actual_result)
        self.assertEqual(expected_result_exhibition, actual_result_exhibition)

    def test_remove_exhibition_with_more_existing_data(self):
        name = 'Heaven'
        year = 2020

        name_two = 'Exhibition'
        year_two = 2022

        self.gallery.add_exhibition(name, year)
        self.gallery.add_exhibition(name_two, year_two)

        expected_result = f'Exhibition "{name_two}" removed.'
        expected_result_exhibitions = {name: year}

        actual_result = self.gallery.remove_exhibition(name_two)
        actual_result_exhibitions = self.gallery.exhibitions

        self.assertEqual(expected_result, actual_result)
        self.assertEqual(expected_result_exhibitions, actual_result_exhibitions)

    def test_remove_exhibition_with_one_existing_data(self):
        name = 'Heaven'
        year = 2020

        self.gallery.add_exhibition(name, year)

        expected_result = f'Exhibition "{name}" removed.'
        expected_result_exhibitions = {}

        actual_result = self.gallery.remove_exhibition(name)
        actual_result_exhibitions = self.gallery.exhibitions

        self.assertEqual(expected_result, actual_result)
        self.assertEqual(expected_result_exhibitions, actual_result_exhibitions)

    def test_try_to_remove_exhibition_with_not_existing_data(self):
        name = 'Heaven'

        expected_result = f'Exhibition "{name}" not found.'
        expected_result_exhibitions = {}

        actual_result = self.gallery.remove_exhibition(name)
        actual_result_exhibitions = self.gallery.exhibitions

        self.assertEqual(expected_result, actual_result)
        self.assertEqual(expected_result_exhibitions, actual_result_exhibitions)

    def test_list_exhibitions_when_is_open_to_public(self):
        self.gallery.add_exhibition('Heaven', 2020)
        self.gallery.add_exhibition('Exhibition', 2022)
        self.gallery.add_exhibition('Private', 2025)

        expected_result = "Heaven: 2020\n" \
                          "Exhibition: 2022\n" \
                          "Private: 2025"

        actual_result = self.gallery.list_exhibitions()

        self.assertEqual(expected_result, actual_result)

    def test_try_to_list_exhibitions_when_not_open_to_public(self):
        self.gallery.open_to_public = False
        
        self.gallery.add_exhibition('Heaven', 2020)
        self.gallery.add_exhibition('Exhibition', 2022)
        self.gallery.add_exhibition('Private', 2025)

        expected_result = f'Gallery {self.gallery.gallery_name}' \
                          f' is currently closed for public! Check for updates later on.'

        actual_result = self.gallery.list_exhibitions()

        self.assertEqual(expected_result, actual_result)

if __name__ == "__main__":
    main()
