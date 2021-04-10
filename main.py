
i = 1
print("välj en siffra mellan 1 till 10 du har 3 försök på dig att gissa rätt")
name = input(" skriv ditt namn ")
while i <= 3:

    if input("gissa ett nummer : ") == "9":
        print(f"du vann {name}!")
        break
    elif i == 3:
        print(f"{name} förlorade försök igen ")
        break
    i = i + 1











