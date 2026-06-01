import os
import json
root = "C:\\Users\\AA\\Downloads\\popular watch\\Images-20260526T075951Z-3-001\\Images"
files = sorted(f for f in os.listdir(root) if f.lower().endswith('.jpg'))
maisons = [
    'Regal Marine', 'Heritage Atelier', 'Atelier', 'Chronos', 'Observatory Works',
    'Noble Horology', 'Cobalt Studio', 'Noir Precision', 'Urban Travaux', 'Aurum Craft'
]
categories = ['Wristwatch', 'Wristwatch', 'Wristwatch', 'Table Clock', 'Wall Clock']
descriptions = {
    'Wristwatch': 'A refined wristwatch balancing performance and luxury design.',
    'Table Clock': 'A statement table clock crafted for sophisticated interiors.',
    'Wall Clock': 'A distinctive wall clock with precise movement and bold styling.'
}
entries = []
for i, fname in enumerate(files):
    idx = i + 1
    base = os.path.splitext(fname)[0]
    prod_id = base.lower().replace('img-', 'timepiece-').replace('wa', '')
    prod_id = prod_id.replace('_', '-').replace(' ', '-')
    maison = maisons[i % len(maisons)]
    category = categories[i % len(categories)]
    price = 120000 + (i % 50) * 10000 + (i // 50) * 20000
    if price < 120000:
        price = 120000
    if price > 9000000:
        price = 9000000
    new_arrival = (i % 8 == 0)
    if category == 'Wristwatch':
        name = f"{maison.split()[0]} {idx:03d}"
    else:
        name = f"{category} {idx:03d}"
    entries.append({
        'id': prod_id,
        'maison': maison,
        'name': name,
        'category': category,
        'price': price,
        'image': f'Images-20260526T075951Z-3-001/Images/{fname}',
        'description': descriptions[category],
        'specs': {
            'calibre': 'Precision Quartz' if category != 'Wristwatch' else 'Automatic 42-hour',
            'winding': 'Battery-powered' if category != 'Wristwatch' else 'Self-winding',
            'powerReserve': '24 months' if category != 'Wristwatch' else '42 hours',
            'diameter': '220 mm' if category == 'Table Clock' else ('340 mm' if category == 'Wall Clock' else '40 mm'),
            'material': 'Brushed Brass' if category != 'Wristwatch' else 'Stainless Steel',
            'waterproof': 'Indoor use only' if category != 'Wristwatch' else '100 meters',
            'strap': 'N/A' if category != 'Wristwatch' else 'Leather strap'
        },
        'newArrival': new_arrival
    })
js = 'const timepieces = ' + json.dumps(entries, indent=2) + ';\n\n'
js += '''function getAllTimepieces() {
  return timepieces;
}

function getNewArrivals() {
  return timepieces.filter(item => item.newArrival);
}

function getTimepieceById(id) {
  if (!id) return null;
  return timepieces.find(watch => watch.id === id);
}

function formatCurrency(amount) {
  return new Intl.NumberFormat('en-IN', {
    style: 'currency',
    currency: 'INR',
    maximumFractionDigits: 0,
  }).format(amount);
}
'''
with open('js/products.js', 'w', encoding='utf-8') as f:
    f.write(js)
print(f'Wrote js/products.js with {len(entries)} products.')
