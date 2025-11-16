
https://www.reddit.com/r/interviews/comments/1olihm4/50_leetcode_questions_you_must_practice_before/

# 50 LeetCode Questions You Must Practice Before Your Google Interview (August 2025 Edition)

I tracked every Google interview question reported across LeetCode discussions, Blind, interview forums, and various sources for the past year. After analyzing 200+ recent Google interview experiences (2024–2025), these 50 problems cover ~87% of what's actually being asked in Google coding interviews.

This list is data-driven: problems repeat across reports, with clear tiers based on frequency and interview stage.

---

## The Context
- Coverage: L3–L6 positions (reported experiences Jan 2024 — Aug 2025).  
- Trend: Post-hiring-freeze interviews pull from a tighter problem pool; predictability increased.  
- Use: Focus on patterns and clean implementation; complexity analysis matters more than perfect edge-case coverage for hardest problems.

---

## The 50 Questions (Ranked by Actual Frequency)

### Tier 1 — The Absolute Must-Knows (Appear in 40%+ of interviews)
These dominate Google interview reports:
- `[200]` Number of Islands — BFS / DFS — **47%**
- `[146]` LRU Cache — design — **45%**
- `[42]` Trapping Rain Water — two-pointers / stack — **43%**
- `[56]` Merge Intervals — sorting — **42%**
- `[297]` Serialize and Deserialize Binary Tree — design — **41%**
- `[139]` Word Break — DP — **39%**
- `[133]` Clone Graph — graph / BFS-DFS — **38%**
- `[208]` Implement Trie — design — **37%**
- `[239]` Sliding Window Maximum — monotonic deque — **36%**
- `[560]` Subarray Sum Equals K — prefix + hashmap — **35%**

### Tier 2 — High Frequency (20–35%)
Weekly appearances in reports:
- `[23]` Merge k Sorted Lists — heap / merge  
- `[128]` Longest Consecutive Sequence — hashing  
- `[295]` Find Median from Data Stream — two heaps  
- `[380]` Insert Delete GetRandom O(1) — design  
- `[394]` Decode String — stack  
- `[269]` Alien Dictionary — topological sort  
- `[340]` Longest Substring with At Most K Distinct — sliding window  
- `[417]` Pacific Atlantic Water Flow — multi-source BFS/DFS  
- `[684]` Redundant Connection — union-find  
- `[494]` Target Sum — DP / subset sum

### Tier 3 — The Differentiators (L5+ and final rounds — 10–20%)
Used to separate senior candidates:
- `[4]` Median of Two Sorted Arrays — binary search on answer  
- `[10]` Regular Expression Matching — DP  
- `[218]` The Skyline Problem — sweep line / heap  
- `[224]` Basic Calculator — stack / parsing  
- `[282]` Expression Add Operators — backtracking  
- `[315]` Count of Smaller Numbers After Self — BIT / merge sort  
- `[332]` Reconstruct Itinerary — Eulerian path  
- `[460]` LFU Cache — design  
- `[685]` Redundant Connection II — union-find + directed  
- `[727]` Minimum Window Subsequence — DP / two-pass

### Tier 4 — The Specialists (System-design coding hybrids — 5–10%)
System-design hybrids and specialized patterns:
- `[31]` Next Permutation — array manipulation  
- `[57]` Insert Interval — intervals  
- `[212]` Word Search II — Trie + DFS  
- `[240]` Search a 2D Matrix II — 2-pointer grid  
- `[261]` Graph Valid Tree — union-find / BFS  
- `[271]` Encode and Decode Strings — design  
- `[310]` Minimum Height Trees — graph trimming  
- `[329]` Longest Increasing Path in a Matrix — DFS + memo  
- `[336]` Palindrome Pairs — trie / hashing  
- `[354]` Russian Doll Envelopes — LIS variant  
- `[363]` Max Sum of Rectangle No Larger Than K — prefix + TreeSet  
- `[378]` Kth Smallest Element in a Sorted Matrix — heap / binary search  
- `[399]` Evaluate Division — graph / union-find  
- `[406]` Queue Reconstruction by Height — greedy sorting  
- `[421]` Maximum XOR of Two Numbers — bit trie  
- `[425]` Word Squares — trie / backtracking  
- `[480]` Sliding Window Median — heaps / balanced BST  
- `[490]` The Maze — BFS / DFS variants  
- `[652]` Find Duplicate Subtrees — tree hashing  
- `[668]` Kth Smallest Number in Multiplication Table — binary search on answer

---

## Patterns We've Noticed
- Phone screens (45 min): ~82% pick from Tiers 1–2. Expect a medium or medium-hard problem. `Islands (200)` and `LRU (146)` dominate.  
- Onsite Rounds 1–2: Mix of Tiers 1–2 with occasional Tier 3. Sliding-window problems spike.  
- Onsite Rounds 3–4: More Tier 3–4; these separate L4 from L5+.  
- Time management: Successful candidates average ~25 min for Tier 1–2, ~35 min for Tier 3–4. Clear approach and complexity analysis matter more than fully polished hardest solutions.

---

## What's Changed in 2025
- Graph problems surged (~+30%). Union-find rose from ~8% to ~14%.  
- Pure classic DP decreased (e.g., Edit Distance down ~40%); DP tends to be embedded within other patterns.  
- Design hybrids increased: caches, serialize/deserialize, encode/decode — now ~35% of interviews (was ~20% last year).

---

## How to Use This List Effectively
- Weeks 1–2: Master Tier 1. Do each problem three times: brute force, optimized, then from memory.  
- Weeks 3–4: Finish Tier 2. Emphasize pattern recognition (e.g., "k distinct" -> sliding window).  
- Weeks 5–6: Sample Tier 3–4 based on target level. L3–L4: light touch. L5+: deep practice.  
- Daily routine: Top candidates practice 3–4 problems/day for ~2 hours. Focus on understanding patterns, trade-offs, and common follow-ups.

---

## The Resource
A live database (LeetWho.com) tracks reported Google coding interview questions, rounds, and accepted approaches. It includes solution patterns, accepted complexities, and common follow-ups (e.g., “[200] Islands follow-up: count distinct islands” appears in ~23% of cases).

---

