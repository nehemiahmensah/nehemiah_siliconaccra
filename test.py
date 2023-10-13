import gooeypie as gp

# def login(event):
#     if pass_inp.text == 'bestpassword':
#         status_lbl.text = '✔ Access granted!'
#     else:
#         status_lbl.text = '❌ Access denied!'

# app = gp.GooeyPieApp('Login')

# user_lbl = gp.Label(app, "Username")
# user_inp = gp.Input(app)
# pass_lbl = gp.Label(app, "Password")
# pass_inp = gp.Secret(app)
# login_btn = gp.Button(app, 'Login', login)
# status_lbl = gp.Label(app, '')

# app.set_grid(4, 2)
# app.add(user_lbl, 1, 1)
# app.add(user_inp, 1, 2)
# app.add(pass_lbl, 2, 1)
# app.add(pass_inp, 2, 2)
# app.add(login_btn, 3, 2)
# app.add(status_lbl, 4, 2)

# app.run()




def menu_select(event):
    # Make a 'breadcrumb' using the menu information from the event object
    menu_path = ' > '.join(event.menu)
    status.text = menu_path

app = gp.GooeyPieApp('GooeyPie Menus')
app.set_size(300, 100)

app.add_menu_item('Menu 1', 'Item 1', menu_select)
app.add_menu_item('Menu 1', 'Item 2', menu_select)
app.add_submenu_item('Menu 1', 'Submenu 1', 'Submenu Item 1', menu_select)
app.add_submenu_item('Menu 1', 'Submenu 1', 'Submenu Item 2', menu_select)

app.add_menu_radios('Menu 2', ['Radio 1', 'Radio 2', 'Radio 3'], menu_select)
app.add_menu_separator('Menu 2')
app.add_submenu_radios('Menu 2', 'Submenu 2', ['Radio 1', 'Radio 2', 'Radio 3'], menu_select)

app.add_menu_checkbox('Menu 3', 'Check 1', menu_select)
app.add_menu_checkbox('Menu 3', 'Check 2', menu_select)
app.add_submenu_checkbox('Menu 3', 'Submenu 3', 'Check 1', menu_select)

app.set_menu_checkbox('Menu 3', 'Check 2', True)

status = gp.Label(app, 'Select a menu')
app.set_grid(1, 1)
app.add(status, 1, 1, align='center', stretch=True)

app.run()