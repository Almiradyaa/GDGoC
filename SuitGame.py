
def playgame():
    choices = ["batu", "gunting", "kertas"]
    playerHearts = 3
    botHearts = 3

    print("Ini permainan suit, pilih antara batu, gunting, atau kertas!")
    print("Kamu dan bot masing-masing punya 3 nyawa.")

    while playerHearts > 0 and botHearts > 0:
        botChoices = random.choice(choices)
        playerChoices = input("Masukkan pilihanmu: ")

        print("Kamu memilih:", player_choices)
        print("Bot memilih:", bot_choices)

        if botChoices == playerChoices:
            print("Hasilnya seri!")
        elif (botChoices == "Batu" and playerChoices == "Gunting") or (botChoices == "Kertas" and playerChoices == "Batu") or (botChoices == "Gunting" and playerChoices == "Kertas"):
            print("Kamu kalah, ayo coba lagi!")
            playerHearts -= 1
        else:
            print("Yeay,Kamu menang!")
            botHearts -= 1

        print(f"Nyawa kamu: {playerHearts}")
        print(f"Nyawa bot: {botHearts}\n")

    if playerHearts == 0:
        print("Huhuu, kamu kalah! Bot menang.")
    else:
        print("Yippiy, kamu menang! Bot kalah.")

playgame()
