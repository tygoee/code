directions: List[number] = []
mine_down = False
block = 0
saved_orientation = 0
saved_location: Position = None
face_player = False
branch_mine = False
break_trees = False
turn = 0
travelled = 0
facing = 0
direction2 = 0
direction = 0
diff_z = 0
diff_x = 0
degrees: List[number] = []


def on_forever():
    if face_player:
        facePlayer()


loops.forever(on_forever)


def on_on_chat(amount):
    agent.move(LEFT, amount)


def on_on_chat2(amount6):
    agent.move(RIGHT, amount6)


def on_on_chat3(amount5):
    agent.move(BACK, amount5)


def on_on_chat4():
    global face_player

    face_player = not (face_player)


def on_on_chat5(amount4):
    agent.move(UP, amount4)


def on_on_chat6():
    agent.move(UP, 1)
    agent.move(DOWN, 1)


def on_on_chat7(amount2):
    if amount2 == 1:
        agent.turn(RIGHT_TURN)
    elif amount2 == 2:
        agent.turn(RIGHT_TURN)
        agent.turn(RIGHT_TURN)
    elif amount2 == 3:
        agent.turn(LEFT_TURN)


def on_on_chat8():
    agent.teleport_to_player()


def on_on_chat9(level):
    global mine_down

    mine_down = not (mine_down)
    mineDown(level)


def on_on_chat10(amount7):
    agent.move(DOWN, amount7)


def on_on_chat11():
    global branch_mine

    branch_mine = not (branch_mine)
    branchMine()


def on_on_chat12(width2):
    global break_trees

    if width2:
        break_trees = not (break_trees)
        breakTrees(width2)


def on_on_chat13(amount3):
    agent.move(FORWARD, amount3)


player.on_chat("left", on_on_chat)
player.on_chat("right", on_on_chat2)
player.on_chat("back", on_on_chat3)
player.on_chat("face", on_on_chat4)
player.on_chat("up", on_on_chat5)
player.on_chat("jump", on_on_chat6)
player.on_chat("turn", on_on_chat7)
player.on_chat("toplayer", on_on_chat8)
player.on_chat("minedown", on_on_chat9)
player.on_chat("down", on_on_chat10)
player.on_chat("branchmine", on_on_chat11)
player.on_chat("minetrees", on_on_chat12)
player.on_chat("forward", on_on_chat13)


def getDirection():
    global diff_x, diff_z, direction, direction2

    diff_x = player.position().get_value(
        Axis.X) - agent.get_position().get_value(Axis.X)
    diff_z = player.position().get_value(
        Axis.Z) - agent.get_position().get_value(Axis.Z)

    if diff_x < 0:
        direction = WEST
    else:
        direction = EAST

    if diff_z < 0:
        direction2 = NORTH
    else:
        direction2 = SOUTH

    if abs(diff_x) >= abs(diff_z):
        return [direction, abs(diff_x)]
    else:
        return [direction2, abs(diff_z)]


def face(direction3: number):
    global facing

    facing = toDirection(agent.get_orientation())

    if facing == NORTH and direction3 == WEST:
        agent.turn(LEFT_TURN)
        facing = toDirection(agent.get_orientation())
    elif facing == WEST and direction3 == NORTH:
        agent.turn(RIGHT_TURN)
        facing = toDirection(agent.get_orientation())

    while facing != direction3:
        if facing < direction3:
            agent.turn(RIGHT_TURN)
            facing = toDirection(agent.get_orientation())
        else:
            agent.turn(LEFT_TURN)
            facing = toDirection(agent.get_orientation())


def breakTrees(width: number):
    global travelled, turn

    travelled = 0
    turn = LEFT_TURN

    while break_trees:
        while agent.detect(AgentDetection.BLOCK, FORWARD) and not (agent.detect(AgentDetection.BLOCK, UP)):
            agent.move(UP, 1)

        agent.move(FORWARD, 1)

        while not (agent.detect(AgentDetection.BLOCK, DOWN)):
            agent.move(DOWN, 1)

        mineTree()
        travelled += 1

        if travelled >= width:
            agent.turn(turn)

            for index in range(3):
                while agent.detect(AgentDetection.BLOCK, FORWARD) and not (agent.detect(AgentDetection.BLOCK, UP)):
                    agent.move(UP, 1)
                agent.move(FORWARD, 1)
                while not (agent.detect(AgentDetection.BLOCK, DOWN)):
                    agent.move(DOWN, 1)

            agent.turn(turn)
            travelled = 0

            if turn == LEFT_TURN:
                turn = RIGHT_TURN
            else:
                turn = LEFT_TURN


def facePlayer():
    face(getDirection()[0])


def branchMine():
    while branch_mine:
        if agent.detect(AgentDetection.BLOCK, FORWARD):
            agent.destroy(FORWARD)

            if agent.detect(AgentDetection.BLOCK, UP):
                agent.destroy(UP)

            agent.move(UP, 1)

            if agent.detect(AgentDetection.BLOCK, FORWARD):
                agent.destroy(FORWARD)

            agent.move(DOWN, 1)
            agent.collect_all()
            agent.turn(LEFT_TURN)

            for index2 in range(3):
                if agent.detect(AgentDetection.BLOCK, FORWARD):
                    agent.destroy(FORWARD)

                agent.move(UP, 1)

                if agent.detect(AgentDetection.BLOCK, FORWARD):
                    agent.destroy(FORWARD)

                agent.move(DOWN, 1)
                agent.move(FORWARD, 1)
                agent.collect_all()

            agent.turn(RIGHT_TURN)
            agent.turn(RIGHT_TURN)

            for index3 in range(3):
                agent.move(FORWARD, 1)

            for index4 in range(3):
                if agent.detect(AgentDetection.BLOCK, FORWARD):
                    agent.destroy(FORWARD)

                agent.move(UP, 1)

                if agent.detect(AgentDetection.BLOCK, FORWARD):
                    agent.destroy(FORWARD)

                agent.move(DOWN, 1)
                agent.move(FORWARD, 1)
                agent.collect_all()

            agent.turn(LEFT_TURN)
            agent.turn(LEFT_TURN)

            for index5 in range(3):
                agent.move(FORWARD, 1)

            agent.turn(RIGHT_TURN)

        else:
            agent.move(FORWARD, 1)

        for index6 in range(4):
            if agent.detect(AgentDetection.BLOCK, FORWARD):
                agent.destroy(FORWARD)

                if agent.detect(AgentDetection.BLOCK, UP):
                    agent.destroy(UP)

                agent.move(UP, 1)

                if agent.detect(AgentDetection.BLOCK, FORWARD):
                    agent.destroy(FORWARD)

                agent.move(DOWN, 1)
                agent.collect_all()
                agent.move(FORWARD, 1)
            else:
                agent.move(FORWARD, 1)


def mineTree():
    global saved_location, saved_orientation, block

    saved_location = agent.get_position()
    saved_orientation = toDirection(agent.get_orientation())

    for side in [LEFT, RIGHT, FORWARD]:
        block = agent.inspect(AgentInspection.BLOCK, side)

        if blocks.name_of_block(block).includes("Leaves"):
            agent.destroy(side)
        elif blocks.name_of_block(block).includes("Log"):
            agent.destroy(side)
            agent.move(side, 1)
            agent.collect_all()

            if blocks.name_of_block(agent.inspect(AgentInspection.BLOCK, DOWN)).includes("Log"):
                agent.destroy(DOWN)
                agent.move(DOWN, 1)
                agent.move(UP, 1)
                agent.collect_all()

            while blocks.name_of_block(agent.inspect(AgentInspection.BLOCK, UP)).includes("Log"):
                agent.destroy(UP)
                agent.collect_all()
                agent.move(UP, 1)

            agent.teleport(saved_location, saved_orientation)


def mineDown(level2: number):
    while mine_down and not (agent.get_position().get_value(Axis.Y) <= level2):
        if agent.detect(AgentDetection.BLOCK, FORWARD):
            agent.destroy(FORWARD)

        if agent.detect(AgentDetection.BLOCK, DOWN):
            agent.destroy(DOWN)

        agent.move(DOWN, 1)
        agent.collect_all()

        if agent.detect(AgentDetection.BLOCK, FORWARD):
            agent.destroy(FORWARD)

        agent.move(FORWARD, 1)
        agent.collect_all()


def fromPlayer(blocks2: number):
    global diff_x, diff_z

    diff_x = abs(player.position().get_value(Axis.X) -
                 agent.get_position().get_value(Axis.X))
    diff_z = abs(player.position().get_value(Axis.Z) -
                 agent.get_position().get_value(Axis.Z))

    if diff_x < blocks2 and diff_z < blocks2:
        return True
    else:
        return False


def toDirection(degree: number):
    global degrees, directions

    degrees = [-180, -90, 0, 90]
    directions = [NORTH, EAST, SOUTH, WEST]

    return directions[degrees.index(degree)]


def round2(number: number, multiple: number):
    return Math.round(number / multiple) * multiple
