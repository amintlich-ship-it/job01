def time_to_text(minutes):
    """Affiche une durée en minutes sous la forme « X heures et Y minutes »."""
    if not isinstance(minutes, int) or isinstance(minutes, bool):
        print(f"{minutes!r} : erreur, il faut un nombre entier de minutes")
    elif minutes < 0:
        print(f"{minutes} : erreur, le nombre de minutes doit être positif")
    else:
        heures, reste = divmod(minutes, 60)
        print(f"{heures} heures et {reste} minutes")