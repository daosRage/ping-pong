

setting_win = {
    "WIDTH": 800,
    "HEIGHT": 600
}
setting_ball = {
    "RADIUS": 20,
    "SPEED": 8
}
setting_board = {
    "WIDTH": 20,
    "HEIGHT": 100
}

start_game = {
    "LEFT_PLAYER": (15, setting_win["HEIGHT"] // 2 - setting_board["HEIGHT"] // 2),
    "RIGHT_PLAYER": (setting_win["WIDTH"] - 20 - 15, setting_win["HEIGHT"] // 2 - setting_board["HEIGHT"] // 2),
    "BALL": {
        "START": (setting_win["WIDTH"] // 2, setting_win["HEIGHT"] // 2),
        "LEFT_PLAYER": -setting_ball["SPEED"],
        "RIGHT_PLAYER": setting_ball["SPEED"]
    }
}