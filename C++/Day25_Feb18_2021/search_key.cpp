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

void deleteKey(Node** head_ref,int key){
    Node* curr_node = *head_ref;
    if(curr_node->data == key){
        *head_ref = (*head_ref)->next;
        delete curr_node;
        return;
    }
    while (curr_node->next->data != key)
    {
        curr_node = curr_node->next;
    }
    Node* temp_node = curr_node->next;
    curr_node->next = curr_node->next->next;
    delete temp_node;
    
}

void deletePos(Node** head_ref, int position){
    Node* curr_node = *head_ref;
    if(position == 0){
        *head_ref = (*head_ref)->next;
        delete curr_node;
        return;
    }
    int target_pos = 1;
    while(curr_node->next != NULL){
        if(target_pos==position){
            Node* temp_node = curr_node->next;
            curr_node->next = curr_node->next->next;
            delete temp_node;
            return;

        }
        curr_node = curr_node->next;
        target_pos++;

    }
}

void deleteLinkedList(Node** head_ref){
    Node* curr_node = *head_ref;
    if (!*head_ref){
        return;
    }
    while(curr_node->next != NULL){
        Node* temp_node = curr_node;
        curr_node = curr_node->next;
        delete curr_node;
    }
    *head_ref = NULL;
}

int length_iterative(Node* head){
    if(!head){
        return 0;
    }
    Node* curr_node = head;
    int count = 0;
    while(curr_node != NULL){
        curr_node = curr_node->next;
        count++;
    }
    return count;
}

int length_recursive(Node* head){
    if(!head){
        return 0;
    }
    else{
        return 1 + length_recursive(head->next);
    }
}

bool search_key_iteration(Node* head,int key){
    if(!head){
        cout<<"Linked List is empty!"<<"\n";
    }
    Node* curr_node = head;
    while(curr_node !=NULL){
        if(curr_node->data == key){
            return true;
        }
        curr_node=curr_node->next;
    }
    return false;
}

bool search_key_recursion(Node* head,int key){
    if(!head){
        return 0;
    }
    if(head->data == key){
        return true;
    }
    else{
        return search_key_recursion(head->next,key);
    }
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

    //search for element in the linked list (iteration)
    int key1 = 7;
    bool check_key1 = search_key_iteration(head,key1);
    cout<<check_key1<<'\n';
    int key2 = 45;
    bool check_key2 = search_key_iteration(head,key2);
    cout<<check_key2<<'\n';

    //search for element in the linked list (recursion)
    key1 = 7;
    check_key1 = search_key_recursion(head,key1);
    cout<<check_key1<<'\n';
    key2 = 45;
    check_key2 = search_key_recursion(head,key2);
    cout<<check_key2<<'\n';

    return 0;

}