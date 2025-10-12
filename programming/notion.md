# GET
## database
### method to get
GET /v1/databases/{database_id}
### respose keys
- object
- id
- created_time
- last_ended_time
- title
- description
- properties
- parent
- url
- archived
## page
### method to get 
GET /v1/pages/{page_id}
### response keys
- object
- id
- created_time
- last_edited_time
- arhived
- parent
- properties
- url
## block
### method to get
GET /v1/blocks/{block_id}
GET /v1/blocks/{block_id}/children
### respose keys
- object
- id
- created_time
- last_edited_time
- has_children
- archived
- type
- type-specific field
- results
- next_cursor
- has_more
## user
### method to get
GET /v1/users/{user_id}
GET /v1/users
### response keys
- object
- id
- type
- person
- name
- avatar_url
## workspace