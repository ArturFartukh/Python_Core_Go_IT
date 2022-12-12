def get_favorites(contacts):
    return list(filter(lambda x: x["favorite"], contacts))


# contact_list = [
#     {
#         "name": "Allen Raymond",
#         "email": "nulla.ante@vestibul.co.uk",
#         "phone": "(992) 914-3792",
#         "favorite": False
#     },
#     {
#         "name": "Artur Fartukh",
#         "email": "ar4ik.8933@vestibul.co.uk",
#         "phone": "(067) 914-3792",
#         "favorite": True
#     }]
# print(get_favorites(contact_list))
