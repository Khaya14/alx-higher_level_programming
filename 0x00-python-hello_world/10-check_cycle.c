#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 *
 * @list: pointer to the list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *head;
	listint_t *temp;

	head = list;
	temp = list;
	while (list && head && head->next)
	{
		list = list->next;
		head = head->next->next;

		if (list == head)
		{
			list = temp;
			temp =  head;
			while (1)
			{
				head = temp;
				while (head->next != list && head->next != temp)
				{
					head = head->next;
				}
				if (head->next == list)
					break;

				list = list->next;
			}
			return (1);
		}
	}

	return (0);
}
