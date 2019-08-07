def set_info(name, age):
    if not 0 < age < 100:
        raise ValueError('age erro')
    print('%s is %s years old' % (name, age))
def set_info2(name, age):
    assert 0 < age < 100, 'age erro'
    print('%s is %s years old' % (name, age))
if __name__ == '__main__':
    set_info('tom', 10)
    set_info2('jucker', 1000)