##a simple quiz py3
##no complex logic as it's an example for kids learning py. (so no loop)
##because of the length, a good one to use later to show what looping does

print('Name the capitals!')
print('Instructions:')
print('You will be given a US state.')
print('Give the correct capital to gain a point.')
print('Use only lowercase letters in your answers.')
print('For example:')
print('if the capital is Sacremento, write sacremento with a small s.')
print('Here we go: '+ '\n'*3)

def check_capital (user_cap, answer_cap):
    ## changes to var seen throughout program
    global score
    if user_cap == answer_cap:
        print('Huzzah!')
        score = score +1
        print('Your score: ' + str(score))
score = 0

##py v2.7:
##texas = raw_input('Texas > ')

alabama = input('alabama > ')
check_capital(alabama, 'montgomery')

alaska = input('alaska > ')
check_capital(alaska, 'juneau')

arizona = input('arizona > ')
check_capital(arizona, 'phoenix')

arkansas = input('arkansas > ')
check_capital(arkansas, 'little rock')

california = input('california > ')
check_capital(california, 'sacramento')

colorado = input('colorado > ')
check_capital(colorado, 'denver')

connecticut = input('connecticut > ')
check_capital(connecticut, 'hartford')

delaware = input('delaware > ')
check_capital(delaware, 'dover')

florida = input('florida > ')
check_capital(florida, 'tallahassee')

georgia = input('georgia > ')
check_capital(georgia, 'atlanta')

hawaii = input('hawaii > ')
check_capital(hawaii, 'honolulu')

idaho = input('idaho > ')
check_capital(idaho, 'boise')

illinois = input('illinois > ')
check_capital(illinois, 'springfield')

indiana = input('indiana > ')
check_capital(indiana, 'indianapolis')

iowa = input('iowa > ')
check_capital(iowa, 'des moines')

kansas = input('kansas > ')
check_capital(kansas, 'topeka')

kentucky = input('kentucky > ')
check_capital(kentucky, 'frankfort')

louisiana = input('louisiana > ')
check_capital(louisiana, 'baton rouge')

maine = input('maine > ')
check_capital(maine, 'augusta')

maryland = input('maryland > ')
check_capital(maryland, 'annapolis')

massachusetts = input('massachusetts > ')
check_capital(massachusetts, 'boston')

michigan = input('michigan > ')
check_capital(michigan, 'lansing')

minnesota = input('minnesota > ')
check_capital(minnesota, 'st. paul')

mississippi = input('mississippi > ')
check_capital(mississippi, 'jackson')

missouri = input('missouri > ')
check_capital(missouri, 'jefferson city')

montana = input('montana > ')
check_capital(montana, 'helena')

nebraska = input('nebraska > ')
check_capital(nebraska, 'lincoln')

nevada = input('nevada > ')
check_capital(nevada, 'carson city')

new_hampshire = input('new hampshire > ')
check_capital(new_hampshire, 'concord')

new_jersey = input('new jersey > ')
check_capital(new_jersey, 'trenton')

new_mexico = input('new mexico > ')
check_capital(new_mexico, 'santa fe')

new_york = input('new york > ')
check_capital(new_york, 'albany')

north_carolina = input('north carolina > ')
check_capital(north_carolina, 'raleigh')

north_dakota = input('north dakota > ')
check_capital(north_dakota, 'bismark')

ohio = input('ohio > ')
check_capital(ohio, 'columbus')

oklahoma = input('oklahoma > ')
check_capital(oklahoma, 'oklahoma city')

oregon = input('oregon > ')
check_capital(oregon, 'salem')

pennsylvania = input('pennsylvania > ')
check_capital(pennsylvania, 'harrisburg')

rhode_island = input('rhode island > ')
check_capital(rhode_island, 'providence')

south_carolina = input('south carolina > ')
check_capital(south_carolina, 'columbia')

south_dakota = input('south dakota  > ')
check_capital(south_dakota, 'pierre')

tennessee = input('tennessee > ')
check_capital(tennessee, 'nashville')

texas = input('texas > ')
check_capital(texas, 'austin')

utah = input('utah > ')
check_capital(utah, 'salt lake city')

vermont = input('vermont > ')
check_capital(vermont, 'montpelier')

virginia = input('virginia > ')
check_capital(virginia, 'richmond')

washington = input('washington > ')
check_capital(washington, 'olympia')

west_virginia = input('west virginia > ')
check_capital(west_virginia, 'charleston')

wisconsin = input('wisconsin > ')
check_capital(wisconsin, 'madison')

wyoming = input('wyoming > ')
check_capital(wyoming, 'cheyenne')
