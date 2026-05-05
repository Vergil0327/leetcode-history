/**
 * Definition for singly-linked list.
 */
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
        if (head == nullptr || head->next == nullptr || k == 0) return head;

        int n = 1;
        ListNode* ptr = head;
        while (ptr->next != nullptr) {
            n++;
            ptr = ptr->next;
        }
        ptr->next = head; // form circle

        k %= n;

        ListNode* newTail = head;
        for (int i=0; i<n-k-1; i++) {
            newTail = newTail->next;
        }

        ListNode* newHead = newTail->next;
        newTail->next = nullptr;
        
        return newHead;
    }
};