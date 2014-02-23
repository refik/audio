from django.contrib.auth.models import User
from collections import defaultdict

users = User.objects.all()
grouped_users = defaultdict(list)

# Grabbing them

for user in users:
    try:
        profile = user.profile
    except:
        print 'no profile for: %s' % (user)
        continue

    if not user.is_active:
        print 'not active: %s' % (user)
        continue

    if 'Teklif Formu' not in [t.isim for t in user.profile.sorumluTip.all()]:
        print 'not interested in offers: %s' % (user)
        continue

    for sehir in user.profile.sorumluSehir.all():
        grouped_users[sehir].append(user)

# Classifying them

for sehir in grouped_users.keys():
    people = grouped_users[sehir]
    categorized = {'birincil': [], 'ikincil': [], 'ucuncul': []}

    for person in people:
        for r_type in categorized.keys():
            value = getattr(person.profile, r_type)
            if value is True:
                categorized[r_type].append(user)

    grouped_users[sehir] = categorized

         
