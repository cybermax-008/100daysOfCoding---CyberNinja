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

int main(){
    // Create a empty list
    Node* head = NULL;

    // Add few elements to the list 
    append(&head,2);
    append(&head,3);
    append(&head,5);
    print_list(head);

    //Add an element to the front of the list
    push(&head,7);
    print_list(head);

    //Insert an element after certain element
    insertAfter(head->next->next,4);
    print_list(head);
    return 0;
}
