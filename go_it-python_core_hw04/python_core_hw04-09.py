def is_valid_pin_codes(pin_codes):
    if len(pin_codes) != len(set(pin_codes)) or pin_codes == []:
        return False
    for pin in pin_codes:
        if len(pin) != 4 or not pin.isdigit():
            return False
    return True
