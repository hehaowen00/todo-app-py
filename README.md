# todo-app-py

## Design

- A collection is a set of lists
- A list is a list of items
- A list can be part of multiple collections
- A item contains a description and a status

## Schema

| User | Collection | List | Item | Status |
| ----- | ----- | ----- | ----- | ---- |
| id | id | id | id | id |
| username | name | name | description | name |
| password | user_id | user_id | user_id | colour |
| | lists[] | items[] | list_id | user_id |
| | | | status_id | list_id |
