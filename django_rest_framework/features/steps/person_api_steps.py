from behave import given, when, then
from rest_framework import status
import json

@given(u'a valid Person')
def step_impl(context):
    context.body = {"first_name":"John", "last_name":"Johnson", "age": 45}

@when(u'I call POST for the people API')
def step_impl(context):
    context.response = context.test.client.post('/api/v1/people/', data=json.dumps(context.body), content_type='application/json')

@then(u'a person resource will be created')
def step_impl(context):
    assert context.response.status_code == 201

@given(u'a person missing {attribute}')
def step_impl(context, attribute):
    if attribute == 'first name':
        context.body = {"last_name":"Johnson", "age": 45}
    elif attribute == 'last name':
        context.body = {"first_name":"John", "age": 45}
    elif attribute == 'age':
        context.body = {"first_name":"John", "last_name":"Johnson"}
    else:
        raise ValueError(f'unknown attribute name {attribute}')

@then(u'a bad request response is recieved')
def step_impl(context):
    assert context.response.status_code == 400