def bevezetes():
    neve = str(input("Játékos neve: "))
    szkor = str(input("Játékos szerepköre: "))
    print("I/B:\n")
    if (szkor == "varázsló"):
        print(f"Üdvözlünk {neve}, 2 életed van!")
    elif (szkor == "harcos"):
        print(f"Üdvözlünk {neve}, 10 életed van!")
    else:
        print(f"Üdvözlünk {neve}, 8 életed van!")

