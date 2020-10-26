# The data for your website

data = {
    # Example of a collection
    "recipes": [
        {
            "name": 'סלומון לפנתאון',
            "author": 'נתנאל קלונטר',
			"category":'דגים',
            'description': ".זה מתכון של סלומון",
            'imageUrl': '/shared/images/1.jpg'
        },
        {
            "name": 'פסטה ברוטב שמנת פטריות',
            "author": 'אוראל קקון',
			"category":'פסטות',
            'description': ".זה מתכון של פסטה",
            'imageUrl': '/shared/images/3.jpg'
        },
		{
            "name": 'סלט שורשים',
            "author": 'נתנאל קלונטר',
			"category":'סלטים',
            'description': ".זה מתכון של סלטים",
            'imageUrl': '/shared/images/4.jpg'
        },
    ]
}


def get_data(params):
    index = int(params.pop('_index', 0))
    length = int(params.pop('_length', 0))
    collection = params.pop('_collection')

    filtered_data = list(filter(lambda element: set(params.items()).issubset(set(element.items())),
                           data[collection]))

    return filtered_data[index:index + length] if length > 0 else filtered_data[index:]