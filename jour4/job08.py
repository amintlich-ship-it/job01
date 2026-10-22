def moyenne(note1, note2, note3):
    """Retourne la moyenne de trois notes."""
    return (note1 + note2 + note3) / 3
 
 
def saisir_note(numero):
    """Demande une note entre 0 et 20 jusqu'à ce que la saisie soit valide."""
    while True:
        try:
            note = float(input(f"Entrez la note {numero} (entre 0 et 20) : ").replace(",", "."))
        except ValueError:
            print("Veuillez entrer un nombre valide.")
            continue
        if 0 <= note <= 20:
            return note
        print("La note doit être comprise entre 0 et 20.")