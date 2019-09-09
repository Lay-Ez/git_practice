print("\n  --Добро пожаловать в Нурлат, странник!-- \n")

class TreeNode:
    def __init__(self, story_piece):
        self.story_piece = story_piece
        self.choices = []


    def add_child(self, node):
        self.choices.append(node)


    def traverse(self):
        story_node = self
        print(story_node.story_piece)
        while story_node.choices != []:
            try:
                choice = input("\n Введи 1 или 2 для продолжения истории:\n")
                chosen_index = int(choice) - 1
            except ValueError:
                print("\n Введи цифры 1 или 2, даун блять! \n")
                continue
            if chosen_index > 1 or chosen_index < 0:
                print("\n Ты считать разучился? \n")
                continue
            chosen_child = story_node.choices[chosen_index]
            print(chosen_child.story_piece)
            story_node = chosen_child
        print("\n\n --- Вот такие дела хуль, на этом всё! ---\n\n")


user_name = input("\n Представься, незнакомец \n")
if user_name.lower() == "роман" or user_name.lower() == "рома":
    print("\n\n\n Добро пожаловать домой, {name}! \
(очень классное имя кста!)".format(name = user_name))
else:
    print("\n\n\n Добро пожаловать домой, {name}! \
(какое-то уебанское имя кста, ну да ладно)".format(name = user_name))

story_root = TreeNode("""\n После долгой поездки с тупым водятлом, которого ты нашёл на блаблакар,
ты наконец-то дома. Но что это, не успел ты вылезти из машины, к тебе подошла
толпа местных гопников!
 Что же ты будешь делать?

    1 ) Скажу, что я свой поцык!
    2 ) Достам травмат""".format(name = user_name))

choice_a = TreeNode("""\n Старший гопник говорит, что не знает никакого {name}а.
Такое уебанское имя он точно бы запомнил!
Внезапно у него звонит телефон, и гопники отвлекаются.
Ты пытаешься воспользоваться моментом, но не можешь решить куда бежать.
Куда же ты направишься?

1 ) К гаражам направо
2 ) В сторону парка""".format(name = user_name))

choice_b = TreeNode("""\n Местная гопота в ахуе с твоей дерзости.
Но не имея лучших вариантов, они уходят.
Ты идешь гулять дальше, звонит маман, кушать готово.
Но ты уже обещал своему другане выйти на улку!

Что ты выберешь, {name}?
    1 ) Пойти домой хамкать
    2 ) Какой нахуй хамкать, друзья важнее.""".format(name = user_name))

choice_a_1 = TreeNode("""\n Затерявшись среди гаражей, тебе удается спастись.
Под покровом ночи ты идешь к себе домой и как обычно теребишь своего маленького {name}чика, бестыдник.

        ---Ты смог выжить в нурике!--- """.format(name = user_name.lower()))

choice_a_2 = TreeNode("""\n Пытаясь не попасться никому на глаза, ты аккуратно крадешься по парку.
Но что это, в твоё лицо кто-то тычет членом. О нет!
Это Халим. Хватая тебя за все места он говорит тебе:
 - {name}чик детка, помнишь как ты любил играться с моей катушкой в 9 классе??

        --- Похоже тебе и твоей анальной девственности пришёл конец... --- """.format(name = user_name))

choice_b_1 = TreeNode("""\n Оказалось, что дома тебя ждала ещё большая толпа гопоты (нурик хуле).
Тебя пинают ногами, и нарекают официальным титулом {name}ия апа.
Униженный, ты берешь первое такси и едешь обратно в свой город.

        --- Нурик оказался тебе не по силам... ---""".format(name = user_name))

choice_b_2 = TreeNode("""\n Ты идешь к своему другане, а какие могут быть друзья у {name}а?
Конечно же речь идёт об анальных приятелях.
Ты идешь в гей-клуб под именем "В аналах истории и аналах {name1}а"
Знатно повеселившись со своими секс-рабами Рифатом и Ильназом
ты идешь домой, не в состоянии сидеть, но счастливый!

       --- Ты нашёл свое счастье в нурике! ---""".format(name = user_name, name1 = user_name))

story_root.add_child(choice_a)
story_root.add_child(choice_b)

choice_a.add_child(choice_a_1)
choice_a.add_child(choice_a_2)

choice_b.add_child(choice_b_1)
choice_b.add_child(choice_b_2)

story_root.traverse()
