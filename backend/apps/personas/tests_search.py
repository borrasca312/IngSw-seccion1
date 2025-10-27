from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from datetime import date

from apps.personas.models import Persona
from apps.catalog.models import Zona, Distrito, GrupoScout, Rama


class PersonaSearchAPITests(APITestCase):
    def setUp(self):
        # Minimal catalog setup for Grupo and Rama
        self.zona = Zona.objects.create(codigo="Z1", nombre="Zona 1")
        self.distrito = Distrito.objects.create(codigo="D1", nombre="Distrito 1", zona=self.zona)
        self.grupo_a = GrupoScout.objects.create(codigo="G1", nombre="Grupo Uno", distrito=self.distrito)
        self.grupo_b = GrupoScout.objects.create(codigo="G2", nombre="Grupo Dos", distrito=self.distrito)
        self.rama_tropa = Rama.objects.create(codigo="TROPA", nombre="Tropa")
        self.rama_manada = Rama.objects.create(codigo="MANADA", nombre="Manada")

        # Personas
        self.p1 = Persona.objects.create(
            rut="12.345.678-9",
            nombres="Juan Perez",
            email="juan@example.com",
            fecha_nacimiento=date(2005, 1, 1),  # edad ~20
            grupo=self.grupo_a,
            rama=self.rama_tropa,
        )
        self.p2 = Persona.objects.create(
            rut="98765432-1",
            nombres="Maria Gomez",
            email="maria@example.com",
            fecha_nacimiento=date(2015, 6, 15),  # edad ~10
            grupo=self.grupo_b,
            rama=self.rama_manada,
        )

    def _search(self, **params):
        url = reverse("persons-search")
        return self.client.get(url, params)

    def test_search_by_rut_partial(self):
        resp = self._search(rut="12.345")
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(resp.data["count"], 1)
        ruts = [p["rut"] for p in resp.data["results"]]
        self.assertIn(self.p1.rut, ruts)

    def test_search_by_nombre(self):
        resp = self._search(nombre="Maria")
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        names = [p["nombres"] for p in resp.data["results"]]
        self.assertIn("Maria Gomez", names)

    def test_search_by_grupo_codigo(self):
        resp = self._search(grupo="G1")
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        ids = [p["id"] for p in resp.data["results"]]
        self.assertIn(self.p1.id, ids)
        self.assertNotIn(self.p2.id, ids)

    def test_search_by_rama_codigo(self):
        resp = self._search(rama="MANADA")
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        ids = [p["id"] for p in resp.data["results"]]
        self.assertIn(self.p2.id, ids)
        self.assertNotIn(self.p1.id, ids)

    def test_search_by_age_range(self):
        # edad_max=12 should include p2 (~10) and exclude p1 (~20)
        resp = self._search(edad_max=12)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        ids = [p["id"] for p in resp.data["results"]]
        self.assertIn(self.p2.id, ids)
        self.assertNotIn(self.p1.id, ids)

    def test_pagination_page_size(self):
        resp = self._search(page_size=1)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp.data["count"], 2)
        self.assertEqual(len(resp.data["results"]), 1)
        self.assertIn("next", resp.data)
