from django.core.urlresolvers import reverse
from django.test import TestCase
from django.utils import timezone

# Create your tests here.
from .models import Mineral


# MODEL TEST
class MineralModelTest(TestCase):
    def setUp(self):
        self.mineral = Mineral.objects.create(
            category="Organic",
            streak="Pink",
            optical_properties="Biaxial",
            group="Organic Minerals",
            name="Abelsonite",
            diaphaneity="Semitransparent",
            color="Pink-purple, dark greyish purple, pale purplish red, reddish brown",
            unit_cell="a = 8.508 \u00c5, b = 11.185 \u00c5c=7.299 \u00c5, \u03b1 = 90.85\u00b0\u03b2 = 114.1\u00b0, \u03b3 = 79.99\u00b0Z = 1",
            strunz_classification="10.CA.20",
            mohs_scale_hardness="2\u20133",
            crystal_symmetry="Space group: P1 or P1Point group: 1 or 1",
            cleavage="Probable on {111}",
            formula="C<sub>31</sub>H<sub>32</sub>N<sub>4</sub>Ni",
            luster="Adamantine, sub-metallic",
            crystal_system="Triclinic",
            image_caption="Abelsonite from the Green River Formation, Uintah County, Utah, US",
            image_filename="Abelsonite.jpg"
        )

    def test_mineral_creation(self):
        # query all objects in database
        mineral = Mineral.objects.get(pk=1)

        # the number of items in database must be 1
        self.assertEqual(Mineral.objects.count(), 1)

        # the pk of the item must be 1
        self.assertEqual(mineral.pk, 1)

        # the title of stored item must be the same
        self.assertEqual(mineral.name, 'Abelsonite')

    def test_return_name_when_type_casted_with_str(self):
        mineral = Mineral.objects.get(pk=1)

        result = str(mineral)

        self.assertEqual(result, 'Abelsonite')


# VIEW TEST


class MineralHomePageTestCase(TestCase):
    '''Tests for the home page view'''

    def setUp(self):
        self.mineral1 = Mineral.objects.create(
            category="Organic",
            streak="Pink",
            optical_properties="Biaxial",
            group="Organic Minerals",
            name="Abelsonite",
            diaphaneity="Semitransparent",
            color="Pink-purple, dark greyish purple, pale purplish red, reddish brown",
            unit_cell="a = 8.508 \u00c5, b = 11.185 \u00c5c=7.299 \u00c5, \u03b1 = 90.85\u00b0\u03b2 = 114.1\u00b0, \u03b3 = 79.99\u00b0Z = 1",
            strunz_classification="10.CA.20",
            mohs_scale_hardness="2\u20133",
            crystal_symmetry="Space group: P1 or P1Point group: 1 or 1",
            cleavage="Probable on {111}",
            formula="C<sub>31</sub>H<sub>32</sub>N<sub>4</sub>Ni",
            luster="Adamantine, sub-metallic",
            crystal_system="Triclinic",
            image_caption="Abelsonite from the Green River Formation, Uintah County, Utah, US",
            image_filename="Abelsonite.jpg"
        )

        self.mineral2 = Mineral.objects.create(
            category="Phosphate",
            streak="White",
            optical_properties="Uniaxial(-)",
            group="Phosphates",
            name="Za\u00efrite",
            diaphaneity="Transparent to translucent",
            color="Greenish, greenish white, yellow green.",
            unit_cell="a = 7.015 \u00c5, c = 16.365 \u00c5; Z = 3",
            specific_gravity="4.37",
            strunz_classification="08.BL.13",
            refractive_index="n\u03c9 = 1.820 - 1.830 n\u03b5 = 1.810",
            mohs_scale_hardness="4.5",
            crystal_symmetry="Trigonal, R3m - hexagonal scalenohedral",
            cleavage="None observed",
            formula="<sub>646</sub>.<sub>86</sub> g",
            luster="Vitreous, resinous",
            crystal_system="Trigonal",
            image_caption="Za\u00efrite from Eta-Etu, Kivu, Democratic Republic of Congo (Za\u00efre), (field of view 6\u00a0mm)",
            image_filename="Za\u00efrite.jpg"
        )

        self.resp = self.client.get(reverse('home'))

    def test_return_status_okay(self):
        self.assertEqual(self.resp.status_code, 200)

    def test_return_layouthtml_as_template_used(self):
        self.assertTemplateUsed(self.resp, 'website/layout.html')

    def test_return_homehtml_as_template_used(self):
        self.assertTemplateUsed(self.resp, 'website/home.html')

    # check and see if it passes the list of mineral names to view
    def test_return_list_of_mineral_names(self):

        self.assertIn(self.mineral1, self.resp.context['minerals'])
        self.assertIn(self.mineral2, self.resp.context['minerals'])


class MineralFilterByGroupTestCase(TestCase):
    '''Tests for filter by Group'''

    def setUp(self):
        self.mineral1 = Mineral.objects.create(
            category="Organic",
            streak="Pink",
            optical_properties="Biaxial",
            group="Organic Minerals",
            name="Abelsonite",
            diaphaneity="Semitransparent",
            color="Pink-purple, dark greyish purple, pale purplish red, reddish brown",
            unit_cell="a = 8.508 \u00c5, b = 11.185 \u00c5c=7.299 \u00c5, \u03b1 = 90.85\u00b0\u03b2 = 114.1\u00b0, \u03b3 = 79.99\u00b0Z = 1",
            strunz_classification="10.CA.20",
            mohs_scale_hardness="2\u20133",
            crystal_symmetry="Space group: P1 or P1Point group: 1 or 1",
            cleavage="Probable on {111}",
            formula="C<sub>31</sub>H<sub>32</sub>N<sub>4</sub>Ni",
            luster="Adamantine, sub-metallic",
            crystal_system="Triclinic",
            image_caption="Abelsonite from the Green River Formation, Uintah County, Utah, US",
            image_filename="Abelsonite.jpg"
        )

        self.mineral2 = Mineral.objects.create(
            category="Phosphate",
            streak="White",
            optical_properties="Uniaxial(-)",
            group="Phosphates",
            name="Za\u00efrite",
            diaphaneity="Transparent to translucent",
            color="Greenish, greenish white, yellow green.",
            unit_cell="a = 7.015 \u00c5, c = 16.365 \u00c5; Z = 3",
            specific_gravity="4.37",
            strunz_classification="08.BL.13",
            refractive_index="n\u03c9 = 1.820 - 1.830 n\u03b5 = 1.810",
            mohs_scale_hardness="4.5",
            crystal_symmetry="Trigonal, R3m - hexagonal scalenohedral",
            cleavage="None observed",
            formula="<sub>646</sub>.<sub>86</sub> g",
            luster="Vitreous, resinous",
            crystal_system="Trigonal",
            image_caption="Za\u00efrite from Eta-Etu, Kivu, Democratic Republic of Congo (Za\u00efre), (field of view 6\u00a0mm)",
            image_filename="Za\u00efrite.jpg"
        )

        self.resp_home = self.client.get(reverse('home'))
        self.resp_detail = self.client.get(
            reverse(
                'mineral',
                kwargs={'mineral_pk': self.mineral1.pk}
            ))

    def test_return_status_okay_on_home_page(self):
        self.assertEqual(self.resp_home.status_code, 200)

    def test_return_status_okay_on_detail_page(self):
        self.assertEqual(self.resp_detail.status_code, 200)

    def test_return_status_redirect_on_query(self):
        self.resp_group_detail = self.client.get(
            '/{0}/'.format(self.mineral1.pk),
            {'q_by_group': self.mineral2.group}
        )

        self.assertRedirects(
            self.resp_group_detail,
            '/?q_by_group={0}'.format(self.mineral2.group)
        )

    def test_return_phosphate_if_queried_object_is_phosphates(self):
        self.resp_group_home = self.client.get('/', {
            'q_by_group': self.mineral2.group
        })

        # check and see if self.resp.context['group'] matches
        self.assertIn(
            self.mineral2,
            self.resp_group_home.context['minerals'])


class MineralFilterByFirstLetterTestCase(TestCase):
    '''Tests for filter by first letter'''

    def setUp(self):
        self.mineral1 = Mineral.objects.create(
            category="Organic",
            streak="Pink",
            optical_properties="Biaxial",
            group="Organic Minerals",
            name="Abelsonite",
            diaphaneity="Semitransparent",
            color="Pink-purple, dark greyish purple, pale purplish red, reddish brown",
            unit_cell="a = 8.508 \u00c5, b = 11.185 \u00c5c=7.299 \u00c5, \u03b1 = 90.85\u00b0\u03b2 = 114.1\u00b0, \u03b3 = 79.99\u00b0Z = 1",
            strunz_classification="10.CA.20",
            mohs_scale_hardness="2\u20133",
            crystal_symmetry="Space group: P1 or P1Point group: 1 or 1",
            cleavage="Probable on {111}",
            formula="C<sub>31</sub>H<sub>32</sub>N<sub>4</sub>Ni",
            luster="Adamantine, sub-metallic",
            crystal_system="Triclinic",
            image_caption="Abelsonite from the Green River Formation, Uintah County, Utah, US",
            image_filename="Abelsonite.jpg"
        )

        self.mineral2 = Mineral.objects.create(
            category="Phosphate",
            streak="White",
            optical_properties="Uniaxial(-)",
            group="Phosphates",
            name="Za\u00efrite",
            diaphaneity="Transparent to translucent",
            color="Greenish, greenish white, yellow green.",
            unit_cell="a = 7.015 \u00c5, c = 16.365 \u00c5; Z = 3",
            specific_gravity="4.37",
            strunz_classification="08.BL.13",
            refractive_index="n\u03c9 = 1.820 - 1.830 n\u03b5 = 1.810",
            mohs_scale_hardness="4.5",
            crystal_symmetry="Trigonal, R3m - hexagonal scalenohedral",
            cleavage="None observed",
            formula="<sub>646</sub>.<sub>86</sub> g",
            luster="Vitreous, resinous",
            crystal_system="Trigonal",
            image_caption="Za\u00efrite from Eta-Etu, Kivu, Democratic Republic of Congo (Za\u00efre), (field of view 6\u00a0mm)",
            image_filename="Za\u00efrite.jpg"
        )

    def test_return_status_okay_on_query(self):
        resp = self.client.get('/', {
            'q': 'A'
        })

        self.assertEqual(resp.status_code, 200)

    def test_return_home_page_on_query(self):
        resp = self.client.get('/', {
            'q': 'A'
        })

        self.assertTemplateUsed(resp, 'website/home.html')

    def test_return_elements_with_a_if_queried_with_letter_a(self):
        expected_length = 1
        expected_mineral = self.mineral1

        resp = self.client.get('/', {
            'q': 'A'
        })

        result = resp.context['minerals']
        result_mineral = result[0]
        result_length = len(result)

        self.assertEqual(expected_length, result_length)
        self.assertEqual(expected_mineral, result_mineral)

    def test_return_elements_with_z_if_queried_with_letter_z(self):
        expected_length = 1
        expected_mineral = self.mineral2

        resp = self.client.get('/', {
            'q': 'Z'
        })

        result = resp.context['minerals']
        result_mineral = result[0]
        result_length = len(result)

        self.assertEqual(expected_length, result_length)
        self.assertEqual(expected_mineral, result_mineral)

    def test_return_empty_for_all_other_letters(self):
        expected_length = 0
        expected_mineral = self.mineral2

        for ascii_num in range(97, 123):
            letter = chr(ascii_num)
            if letter == 'a' or letter == 'z':
                continue

            resp = self.client.get('/', {
                'q': letter
            })

            result = resp.context['minerals']
            result_length = len(result)

            self.assertEqual(expected_length, result_length)


class MineralDetailPageTestCase(TestCase):
    '''Tests for the Article detail view'''

    def setUp(self):
        self.mineral = Mineral.objects.create(
            category="Organic",
            streak="Pink",
            optical_properties="Biaxial",
            group="Organic Minerals",
            name="Abelsonite",
            diaphaneity="Semitransparent",
            color="Pink-purple, dark greyish purple, pale purplish red, reddish brown",
            unit_cell="a = 8.508 \u00c5, b = 11.185 \u00c5c=7.299 \u00c5, \u03b1 = 90.85\u00b0\u03b2 = 114.1\u00b0, \u03b3 = 79.99\u00b0Z = 1",
            strunz_classification="10.CA.20",
            mohs_scale_hardness="2\u20133",
            crystal_symmetry="Space group: P1 or P1Point group: 1 or 1",
            cleavage="Probable on {111}",
            formula="C<sub>31</sub>H<sub>32</sub>N<sub>4</sub>Ni",
            luster="Adamantine, sub-metallic",
            crystal_system="Triclinic",
            image_caption="Abelsonite from the Green River Formation, Uintah County, Utah, US",
            image_filename="Abelsonite.jpg"
        )

        self.resp = self.client.get(reverse(
            'mineral',
            kwargs={'mineral_pk': self.mineral.pk}
        ))

    def test_return_status_okay(self):
        self.assertEqual(self.resp.status_code, 200)

    def test_return_layouthtml_as_template_used(self):
        self.assertTemplateUsed(self.resp, 'website/layout.html')

    def test_return_detailhtml_as_template_used(self):
        self.assertTemplateUsed(self.resp, 'website/detail.html')

    def test_return_info_of_added_mineral(self):
        self.assertContains(self.resp, self.mineral.name)