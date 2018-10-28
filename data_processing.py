class Calculator:
    def __init__(self, data):
        self.data = data

    def sum_of_passengers(self):
        return sum([x.number_of_fellow_passengers for x in self.data])

    def sum_of_passengers_with_compensation(self):
        return sum([x.number_of_fellow_passengers for x in self.data if x.did_receive_compensation])   

    def sum_of_compensations(self):
        return sum(x.total_compensation_amount for x in self.data)

    def distribution(self):
        return self.sum_of_passengers() / len(self.data)

    def average_compensation(self):
        return self.sum_of_compensations()/self.sum_of_passengers()

    def count_airline_records(self, airline):
        return len([x.airline_code for x in self.data if x.airline_code == airline])
    
    def most_popular_airline(self):
        airlines = list(set([x.airline_code for x in self.data]))
        rank = []
        for airline in airlines:
            rank.append(self.count_airline_records(airline))
        return [airlines[i] for i,x in enumerate(rank) if x == max(rank)]

    def percet_of_passengers_with_compensation(self):
        return (self.sum_of_passengers_with_compensation()/self.sum_of_passengers()) * 100
