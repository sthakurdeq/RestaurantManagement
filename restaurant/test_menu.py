from unittest.mock import MagicMock, patch

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from restaurant.factory_boy import ItemFactory, MenuFactory, RestaurantFactory


class TestMenuAPIs(APITestCase):
    """
    Test the Menu api
    GET, POST, PUT, PATCH, DELETE
    """

    headers = {"Authorization": "Token token_key"}

    @patch(
        "rest_framework.authtoken.models.Token",
        MagicMock(return_value=headers["Authorization"]),
    )
    def test_menu_list(self):
        # method to test the getting list of menus
        created_menu = []
        for j in range(3):
            restaurant = RestaurantFactory()
            menu = MenuFactory(restaurants=restaurant)
            created_item = [ItemFactory() for i in range(3)]
            menu.item.add(created_item[0])
            menu.item.add(created_item[1])
            menu.item.add(created_item[2])
            created_menu.append(menu)
        res = self.client.get(
            reverse("menu-list"),
            format="json",
            HTTP_AUTHORIZATION="Token token_key",
        )
        result_data = res.json()
        assert res.status_code == status.HTTP_200_OK
        for menu_data, result in zip(created_menu, result_data):
            assert str(menu_data.id) == result["id"]
            assert str(menu_data.restaurants_id) == result["restaurants"]
            assert menu_data.day == result["day"]
            item_ids = [item_result["id"] for item_result in result["items"]]
            assert item_ids == [str(a.id) for a in menu_data.item.all()]

    @patch(
        "rest_framework.authtoken.models.Token",
        MagicMock(return_value=headers["Authorization"]),
    )
    def test_menu_creation(self):
        # method to test the creation of menu
        created_item = [str(ItemFactory().id) for i in range(3)]
        restaurant = RestaurantFactory()
        data = {
            "restaurants": restaurant.id,
            "day": "MON",
            "item": created_item
        }


        res = self.client.post(
            reverse("menu-list"),
            data=data,
            format="json",
            HTTP_AUTHORIZATION="Token token_key",
        )
        result_data = res.json()

        assert res.status_code == status.HTTP_201_CREATED
        assert result_data["restaurants"] == str(data["restaurants"])
        assert result_data["day"] == data["day"]
        item_ids = [item_result for item_result in result_data["item"]]
        assert set(item_ids) == set(data['item'])

    @patch(
        "rest_framework.authtoken.models.Token",
        MagicMock(return_value=headers["Authorization"]),
    )
    def test_menu_detail(self):
        # method to test the getting prticular of menu
        restaurant = RestaurantFactory()
        menu = MenuFactory(restaurants=restaurant)
        created_item = [ItemFactory() for a in range(3)]
        menu.item.add(created_item[0])
        menu.item.add(created_item[1])
        menu.item.add(created_item[2])
        res = self.client.get(
            reverse("menu-detail", args=[str(menu.id)]),
            format="json",
            HTTP_AUTHORIZATION="Token token_key",
        )
        result_data = res.json()
        assert res.status_code == status.HTTP_200_OK
        assert str(menu.id) == result_data["id"]
        assert str(menu.restaurants_id) == result_data["restaurants"]
        assert menu.day == result_data["day"]
        item_ids = [item_result for item_result in result_data["item"]]
        assert item_ids == [str(a.id) for a in menu.item.all()]

    @patch(
        "rest_framework.authtoken.models.Token",
        MagicMock(return_value=headers["Authorization"]),
    )
    def test_menu_partial_update(self):
        # method to test the partil updation of menu
        restaurant = RestaurantFactory()
        menu = MenuFactory(restaurants=restaurant)
        created_item = [ItemFactory() for a in range(2)]
        menu.item.add(created_item[0])
        menu.item.add(created_item[1])
        res = self.client.patch(
            reverse("menu-detail", args=[str(menu.id)]),
            format="json",
            HTTP_AUTHORIZATION="Token token_key",
        )
        result_data = res.json()
        assert res.status_code == status.HTTP_200_OK
        assert str(menu.id) == result_data["id"]
        assert str(menu.restaurants_id) == result_data["restaurants"]
        assert menu.day == result_data["day"]
        item_ids = [item_result for item_result in result_data["item"]]
        assert item_ids == [str(a.id) for a in menu.item.all()]

    @patch(
        "rest_framework.authtoken.models.Token",
        MagicMock(return_value=headers["Authorization"]),
    )
    def test_menu_update(self):
        # method to test the updation of menu
        restaurant = RestaurantFactory()
        menu = MenuFactory(restaurants=restaurant)
        created_item = [str(ItemFactory().id) for i in range(3)]
        # menu.item.add(created_item[0])
        # menu.item.add(created_item[1])
        # created_item = [str(ItemFactory().id) for i in range(3)]
        # restaurant = RestaurantFactory()
        data = {
            "restaurants": restaurant.id,
            "day": menu.day,
            "item": created_item
        }
        res = self.client.put(
            reverse("menu-detail", args=[str(menu.id)]),
            data = data,
            format="json",
            HTTP_AUTHORIZATION="Token token_key",
        )
        result_data = res.json()
        # breakpoint()
        assert res.status_code == status.HTTP_200_OK
        assert str(menu.id) == result_data["id"]
        assert str(menu.restaurants_id) == result_data["restaurants"]
        # breakpoint()
        assert menu.day == result_data["day"]
        item_ids = [item_result for item_result in result_data["item"]]
        assert item_ids == [str(a.id) for a in menu.item.all()]

    @patch(
        "rest_framework.authtoken.models.Token",
        MagicMock(return_value=headers["Authorization"]),
    )
    def test_menu_delete(self):
        # method to test the deletion of menu
        restaurant = RestaurantFactory()
        menu = MenuFactory(restaurants=restaurant)
        created_item = [ItemFactory() for a in range(2)]
        menu.item.add(created_item[0])
        menu.item.add(created_item[1])
        res = self.client.delete(
            reverse("menu-detail", args=[str(menu.id)]),
            format="json",
            HTTP_AUTHORIZATION="Token token_key",
        )
        assert res.status_code == status.HTTP_204_NO_CONTENT

    @patch(
        "rest_framework.authtoken.models.Token",
        MagicMock(return_value=headers["Authorization"]),
    )
    def test_today_menu_list(self):
        # method to test the getting list of menus
        created_menu = []
        for j in range(3):
            restaurant = RestaurantFactory()
            menu = MenuFactory(restaurants=restaurant)
            created_item = [ItemFactory() for i in range(3)]
            menu.item.add(created_item[0])
            menu.item.add(created_item[1])
            menu.item.add(created_item[2])
            created_menu.append(menu)
        # breakpoint()
        res = self.client.get(
            reverse("today_menu-list"),
            format="json",
            HTTP_AUTHORIZATION="Token token_key",
        )
        result_data = res.json()
        res = self.client.get(
            reverse("today_menu-list"),
            format="json",
            HTTP_AUTHORIZATION="Token token_key",
        )
        assert res.status_code == status.HTTP_200_OK
        for menu_data, result in zip(created_menu, result_data):
            assert str(menu_data.id) == result["id"]
            assert str(menu_data.restaurants_id) == result["restaurants"]
            assert menu_data.day == result["day"]
            item_ids = [item_result["id"] for item_result in result["items"]]
            assert item_ids == [str(a.id) for a in menu_data.item.all()]