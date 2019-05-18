import json
import datetime
import collections

from kwikapi import API
from typing import Any
from logging import Logger
from kwikapi import Request
from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers

from food.models import Food
from food_delivery.settings import CURRENT_TIMESTAMP


class FoodApp():

    NAME = "Food"
    DESC = "Track the delivery of the foods."

    def get_details(self, **kwargs: Any) -> dict:

        '''
        This API will return the details related to Food.
        **kwargs:
            order_no: order no for the food
            title: title for the delivery task
            dt_created: when order is created
            dt_updated: updated time for the order
            status: order is deliverd or not
            priority: medium/high/low
            task: new/declined/accepted
        Response:
            Returns JSON response whether the record is present in the database or not.

        '''

        if not kwargs:
            food_obj = self._get_response(Food.objects.all())
            return {'details': food_obj}

        collection_fields = [f.name for f in Food._meta.fields]
        inavlid_fields = list(set([x.lower() for x in kwargs.keys()]) - set(collection_fields))

        if inavlid_fields:
            raise Exception('invalid_fields: {}'.format(inavlid_fields))

        if kwargs:
            food_obj = self._get_response(Food.objects.filter(**kwargs))

        return{'details': food_obj}

    def _get_response(self, food_obj: object) -> list:

        records = []
        for food in food_obj:
            records.append({
                "order_no": food.order_no,
            	"title": food.title,
            	"status": food.status,
            	"priority" : food.priority,
            	"task" : food.task,
            })

        return records

    def add_order(self, order_no: str, title: str, status: str, priority: str, task:str) -> dict:

        '''
        Desc:
            Adds order to the database.
        Params:
            order_no: order no for the food
            title: title for the delivery task
            dt_created: when order is created
            dt_updated: updated time for the order
            status: order is deliverd or not
            priority: medium/high/low
            task: new/declined/accepted
        Response:
            Returns the JSON reponse, whether the order added successfully or not.

        '''

        try:
            food_obj = Food.objects.create(order_no=order_no, title=title, status=status, priority=priority, task=task)
            food_obj.save()
        except:
            return {"message": "Order already exists in {}.".format(order_no), "success": False}

        return {"message": "Order added successfully."}


    def delete_order(self, order_no:str) -> dict:

        '''
        Desc:
            This API will delete the order from the database.
        Params:
            order_no: order_no which needs to be deleted
        Response:
            Returns JSON response whether the order is deleted successfully or not from the database.

        '''

        get_order = Food.objects.filter(order_no=order_no)
        if not get_order:
            return {"message": "Order dose not exist in the database", "success": False}

        try:
            get_order.delete()
        except:
            return {"message": "Failed to delete order.", "success": False}

        return {"message": "Order deleted successfully"}


    def update_order(self, order_no:str, **kwargs: Any) -> dict:

        '''
        Desc:
            This API will update the record in the database based on the order_no.
        Params:
            order_no: Name of the order_no which needs to get updated
        **kwargs:
           order_no: order no for the food
           title: title for the delivery task
           dt_created: when order is created
           dt_updated: updated time for the order
           status: order is deliverd or not
           priority: medium/high/low
           task: new/declined/accepted

        '''

        if not kwargs:
            raise Exception('Atleast one argument should be passed to perform an update operation')

        food_obj = Food.objects.filter(order_no=order_no)

        if not food_obj:
            raise Exception('order does not exists')

        collection_fields = [f.name for f in Food._meta.fields]
        invalid_fields = list(set([x.lower() for x in kwargs.keys()]) - set(collection_fields))

        if invalid_fields:
            raise Exception('invalid_fields: {}'.format(invalid_fields))

        try:
            food_obj.update(**kwargs, dt_updated=CURRENT_TIMESTAMP)
            return "Updated record with the given parameters."
        except:
            raise Exception('Failed to update !!')

api = API(Logger)
api.register(FoodApp(), 'v1')
