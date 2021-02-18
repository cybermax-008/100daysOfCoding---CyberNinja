#include<bits/stdc++.h>

using namespace std;

class Node{
    public:
        int data;
    Node* next;
};

void print_list(Node* n){
    if(n == NULL){
        cout << "The linked list is Empty!";
    }
    while(n != NULL){
        cout << n->data<< " ";
        n = n->next;
    }
    cout <<"\n";
}

void push(Node** head_ref, int num){
    Node* new_node = new Node();
    new_node->data = num;
    if(*head_ref == NULL){
        new_node->next = NULL;
        *head_ref = new_node;
        return;
    }
    new_node->next = *head_ref;
    *head_ref = new_node;

}

void insertAfter(Node* prev_node, int num){

    if (prev_node == NULL){
        return;
    }
    Node* new_node = new Node();

    new_node->data = num;
    new_node->next = prev_node->next;
    prev_node->next = new_node;
}

void append(Node** head_ref, int num){
    Node* new_node = new Node();
    new_node->data = num;
    new_node->next = NULL;
    if(*head_ref == NULL){
        *head_ref = new_node;
        return;
    }
    Node* curr_node = *head_ref;
    while(curr_node->next !=NULL){
        curr_node = curr_node->next;
    }
    curr_node->next = new_node;
    
}
void deleteFirstNode(Node** head_ref){
    if(!*head_ref){
        return;
    }
    Node* tempNode = *head_ref;
    *head_ref = (*head_ref)->next;
    delete tempNode;
}

void deleteLastNode(Node* head){
    if(!head){
        return;
    }
    if(head->next == NULL){
        return;
    }
    Node* second_last = head;
    while (second_last->next->next !=NULL){
        second_last =second_last->next;
    }
    delete second_last->next;
    second_last->next = NULL;
}

void deleteAfter(Node* pre_node){
    if(!pre_node){
        return;
    }
    Node* tempNode = pre_node->next;
    pre_node->next = pre_node->next->next;
    delete tempNode;
}

int main(){
    // Create a empty list
    Node* head = NULL;

    //Add few elements to the list 
    append(&head,2);
    append(&head,3);
    append(&head,5);
    append(&head,7);
    append(&head,10);
    append(&head,12);
    append(&head,15);

    //delete the first node
    deleteFirstNode(&head);
    print_list(head);

    //delete the last node
    deleteLastNode(head);
    print_list(head);

    //delete node after certain node
    deleteAfter(head->next->next);
    print_list(head);



    return 0;
}
