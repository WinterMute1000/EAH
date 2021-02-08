class IDGeneratorByName:
    def __init__(self, name_list):
        self.name_list = name_list
        self.id_list = []

    def generate_id_list(self):
        for name in self.name_list:
            # Must string type
            first_name, last_name = name.split()[:2]
            first_name = first_name.lower()
            last_name = last_name.lower()
            number_list = [num for num in range(1, 101)]

            for number in number_list:
                self.id_list.append(first_name + last_name + str(number))
                self.id_list.append(first_name[:1] + last_name + str(number))
                self.id_list.append(first_name + last_name[:1] + str(number))
                self.id_list.append(first_name[:1] + last_name[:1] + str(number))

        return self.id_list


if __name__ == '__main__':
    id_gen = IDGeneratorByName(['Chris Martin', 'Guy Berryman', 'Jonny Buckland', 'Will Champion'])
    print(id_gen.generate_id_list())
