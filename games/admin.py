from django.contrib import admin

from games.models import game1 , game2 , game3 , game4 , game5 , game6

#  game1 
class game1Admin(admin.ModelAdmin):
    list_display = ('fontImage','game_name','Image','rate')
    

admin.site.register(game1, game1Admin)


# game2
class game2Admin(admin.ModelAdmin):
    list_display = ('fontImage','game_name','Image','rate')
    

admin.site.register(game2, game2Admin)


# game3 
class game3Admin(admin.ModelAdmin):
    list_display = ('fontImage','game_name','Image','rate')
    

admin.site.register(game3, game3Admin)

# game4 

class game4Admin(admin.ModelAdmin):
    list_display = ('fontImage','game_name','Image','rate')
    

admin.site.register(game4, game4Admin)

# game5 


class game5Admin(admin.ModelAdmin):
    list_display = ('fontImage','game_name','Image','rate')
    

admin.site.register(game5, game5Admin)

# game6 

class game6Admin(admin.ModelAdmin):
    list_display = ('fontImage','game_name','Image','rate')
    

admin.site.register(game6, game6Admin)


