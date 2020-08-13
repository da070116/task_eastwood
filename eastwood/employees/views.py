from typing import List

from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Employee, Department
from itertools import groupby
from operator import itemgetter


# Dictionary main logic


#
def chunks(items: List[Employee]):
    """
     Logic was taken from here  https://qna.habr.com/q/373740
    Split by groups for the first letter of surname.

    :param items: list of all employees sorted by surname
    :return: generator
    """
    dict_name = []
    for x in items:
        dict_name.append(f"{x.surname} {x.name}#{x.id}")  # Appending an ID simplifies search in view logic
    for letter, names in groupby(sorted(dict_name), key=itemgetter(0)):
        yield list(names)


#
def reshape(items, min_len, max_len):
    """
     Merging the groups with size less then min_len to a size less or equal then max_len
    :param items:   list of names (+id)
    :param min_len: minimal size of each group
    :param max_len: maximal size of each group
    :return: generator
    """
    buffer = []
    for item in items:
        if len(buffer) >= max_len:
            yield sorted(buffer)
            buffer = []
        if len(item) <= min_len:
            buffer += item
        else:
            yield item
    yield sorted(buffer)


def dictionarize(sort_orders: List[Employee]):
    """
    Returns a formatted dict.

    """
    groups_list = reshape(chunks(sort_orders), len(sort_orders) // 3, len(sort_orders) // 5)
    result = {'{}-{}'.format(item[0][0], item[-1][0]): item for item in groups_list}
    return result


# --------------------------------------------------

class EmployeesListView(ListView):
    """
        Default list with all employees.
    """
    model = Employee
    context_object_name = "all_employees"
    paginate_by = 3
    paginate_orphans = 1
    ordering = ['id']


class EmployeesDeptView(ListView):
    """
       Sorted by department view.
    """
    template_name = "employees/employee_dept.html"
    context_object_name = "dept_employees"
    paginate_by = 3
    paginate_orphans = 1
    ordering = ['id']
    dept = None

    def get_queryset(self):
        """

        :return: queryset where employees are belong to required department
        """
        self.dept = get_object_or_404(Department, id=self.kwargs['dept'])
        return Employee.objects.filter(dept=self.dept)

    def get_context_data(self, **kwargs):
        """
            returns context data with dept parameter
        """
        context = super(EmployeesDeptView, self).get_context_data(**kwargs)
        context['dept'] = self.dept
        return context


class EmployeesRecentView(ListView):
    """
        list with employees who is still working
    """
    template_name = "employees/employee_actual.html"
    context_object_name = "recent_employees"
    paginate_by = 3
    paginate_orphans = 5
    ordering = ['id']

    def get_queryset(self):
        """
        :return: queryset where model field ended_work is equal to empty.
        """
        result = Employee.objects.exclude(ended_work__isnull=False)
        return result


class EmployeeDetail(DetailView):
    model = Employee
    context_object_name = "employee"
    queryset = Employee.objects.all()


class EmployeeDictionaryView(ListView):
    """
        Dictionary view.

        Accepts 0 or 1 parameter ("part"). If 0 displays a list of hyperlinks
        that represents the first letter of each employee surname in list.
    """
    template_name = "employees/employee_dict.html"
    context_object_name = "dict"
    dictionary = dictionarize(Employee.objects.all().order_by('surname'))
    paginate_by = 3
    paginate_orphans = 5

    def get_context_data(self, **kwargs):
        """
        :return: display a group of links
        """
        context = super(EmployeeDictionaryView, self).get_context_data(**kwargs)
        keys_dict = {}
        for counter, key in enumerate(self.dictionary.keys()):
            keys_dict[counter] = key
        context["keys"] = keys_dict
        if self.kwargs:
            context["selected_key"] = list(self.dictionary.keys())[self.kwargs['part']]
        print(context)
        return context

    def get_queryset(self):
        """
        :return: a queryset that contains all the employees which surname' first letter
                are in range of the current link
        """
        queryset = []
        if self.kwargs:
            vals = list(self.dictionary.values())
            for item in vals[self.kwargs['part']]:
                id = item.split("#")[1]
                queryset.append(get_object_or_404(Employee, id=id))
        return queryset
