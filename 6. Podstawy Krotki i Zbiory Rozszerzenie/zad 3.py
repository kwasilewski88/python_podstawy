moj_zbior = {'zielony', 'czerwony'}
# moj_zbior = [ 'czerwony']

ulubionych_zbior = {'czerwony', 'niebieski'}
# ulubionych_zbior = ['czerwony']

if moj_zbior == ulubionych_zbior:
    print("sa takie same")
else:
    print("roznia sie")
    print(moj_zbior.intersection(ulubionych_zbior))
    print(moj_zbior.difference(ulubionych_zbior))
    print(ulubionych_zbior.difference(moj_zbior))
