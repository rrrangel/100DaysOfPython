# Assign type to variable wthout assigning a value
age: int
name: str
height: float
is_human: bool


# Assign Data type to a function (param and return)
def police_check(age: int) -> bool:  # type hint
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive


if police_check(12):
    print("You may pass")
else:
    print("Pay a fine.")
