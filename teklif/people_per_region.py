from django.contrib.auth.models import User

def find_region_cities(name):
    try:
        user = User.objects.filter(username=name).get()
        profile = user.profile
    except:
        return []

    if not user.is_active:
        return []

    return profile.sorumluSehir.all()

grouped_regions = {}
region_people = {
    # Tasra 1
    'Ankara': 'mahmutarslan',
    'Bursa': 'rizaseyri',
    'Antalya': 'mertgulveren',
    'Eskisehir': 'yakupozel',
    'Kayseri': 'recaicitak',
    'Diyarbakir': 'fatihpoyraz',
    'Mersin': 'denizfalcioglu',
    'Malatya': 'gokhangunhan',

    # Tasra 2
    'Izmir': 'gokhandurak',
    'Adana': 'ahmetbulucu',
    'Kocaeli': 'erdemcil',
    'Gaziantep': 'cemcelik',
    'Konya': 'aliakyel',
    'Samsun': 'barisozturk',
    'Trabzon': 'temelbesli',
    'Trakya': 'ismailpekdogan',

    # Rumeli
    'Rumeli': 'buraktokmak',
    'Anadolu': 'sinangungor',
}

for region, user_name in region_people.items():
    cities = find_region_cities(user_name)
    if len(cities) == 0:
        print 'No city found for %s' % region
        continue
    grouped_regions[region] = cities
