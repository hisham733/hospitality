from __future__ import unicode_literals
from frappe import _

def get_data():

	config =  [
		{
			"label": _("Hotels"),
			"icon": "icon-star",
			"items": [
				{
					"type": "doctype",
					"name": "Hotel Room",
					"label": _("Hotel Room"),
				},
				{
					"type": "doctype",
					"name": "Hotel Room Amenity",
					"label": _("Hotel Room Amenity"),
				},
                {
					"type": "doctype",
					"name": "Hotel Room Package",
					"label": _("Hotel Room Package"),
				},
                {
					"type": "doctype",
					"name": "Hotel Room Pricing",
					"label": _("Hotel Room Pricing"),
				},
                {
					"type": "doctype",
					"name": "Hotel Room Pricing Item",
					"label": _("Hotel Room Pricing Item"),
				},
                {
					"type": "doctype",
					"name": "Hotel Room Pricing Package",
					"label": _("Hotel Room Pricing Package"),
				},
                {
					"type": "doctype",
					"name": "Hotel Room Reservation",
					"label": _("Hotel Room Reservation"),
				},
                {
					"type": "doctype",
					"name": "Hotel Room Reservation Item",
					"label": _("Hotel Room Reservation Item"),
				},
                {
					"type": "doctype",
					"name": "Hotel Room Type",
					"label": _("Hotel Room Type"),
				},
                {
					"type": "doctype",
					"name": "Hotel Settings",
					"label": _("Hotel Settings"),
				},
            ]
        },
        {
            "label": _("Restaurant"),
			"icon": "icon-star",
			"items": [

                {
					"type": "doctype",
					"name": "Restaurant",
					"label": _("Restaurant"),
				},
                {
					"type": "doctype",
					"name": "Restaurant Menu",
					"label": _("Restaurant Menu"),
				},
                {
					"type": "doctype",
					"name": "Restaurant Menu Item",
					"label": _("Restaurant Menu Item"),
				},
                {
					"type": "doctype",
					"name": "Restaurant Order Entry",
					"label": _("Restaurant Order Entry"),
				},
                {
					"type": "doctype",
					"name": "Restaurant Order Entry Item",
					"label": _("Restaurant Order Entry Item"),
				},
                {
					"type": "doctype",
					"name": "Restaurant Reservation",
					"label": _("Restaurant Reservation"),
				},
                {
					"type": "doctype",
					"name": "Restaurant Table",
					"label": _("Restaurant Table"),
				}

            ]


        },
    ]
	return config
