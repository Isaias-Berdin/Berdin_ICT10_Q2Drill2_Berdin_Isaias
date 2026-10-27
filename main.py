from pyscript import document, display

def add_glee_member(e):
    document.getElementById("output1").innerHTML = ""
    g7={'Punzalan, Zeauss', 'Delin, Maria', 'Saludar, Kendra', 'Tagle, Ronald'}
    g8={'Abdul, Jibril', 'Eligino, Erich', 'Ballesteros, Nina', 'Moncupa Bella'}
    g9={'Mendoza, Orange', 'Basuil, Anya', 'Llaguno, Alezandra', 'Bacani, Rhiana'}
    g10={'Arada, Hans', 'Berdin, Isaias', 'David, Carlos', 'Taguiga, Gavin'}
    all_grades = g7 | g8 | g9 | g10
    lastname = document.getElementById("input1").value
    firstname = document.getElementById("input2").value
    member_name = (f"{lastname.title()}, {firstname.title()}")
    confirm_member = member_name in all_grades
    new_member_set = {member_name}
    all_members = all_grades | new_member_set
    total_members = len(all_grades | new_member_set)
    member_list = "<br>".join(sorted(all_members))
    document.getElementById("output1").innerHTML = f'All members:<br><br> {member_list}'
    display(f'Total members: {total_members}',target="output1")