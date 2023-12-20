import UI

if __name__=="__main__":
    game = UI.UI()
    game.start()
    

gen = "тут генератор вызываешь"
values = []

for _ in range(5):
    values.append(next(gen))