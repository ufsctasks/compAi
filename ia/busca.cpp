#include <algorithm>
#include <climits>
#include <iostream>
#include <queue>
#include <stdlib.h>
#include <string>
#include <vector>

using namespace std;

int findShortestWay(int maze[5][5], int start[2], int destination[2]) {
  int m = 5, n = 5;
  int res = INT_MAX;
  vector<vector<int>> dirs = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
  vector<string> dirStr = {"r", "l", "d", "u"};
  vector<vector<int>> visited(m, vector<int>(n, 0));
  vector<vector<string>> path(m, vector<string>(n, ""));
  queue<vector<int>> q;
  q.push(start);
  while (!q.empty()) {
    vector<int> cur = q.front();
    q.pop();
    for (int i = 0; i < 4; i++) {
      int x = cur[0], y = cur[1], len = 0;
      string curDir = path[x][y];
      while (x >= 0 && x < m && y >= 0 && y < n && maze[x][y] == 0) {
        if (x == destination[0] && y == destination[1]) {
          if (len < res) {
            res = len;
            path[x][y] = curDir;
          } else if (len == res) {
            path[x][y] += curDir;
          }
          break;
        }
        x += dirs[i][0];
        y += dirs[i][1];
        len++;
      }
      x -= dirs[i][0];
      y -= dirs[i][1];
      if (!visited[x][y]) {
        visited[x][y] = 1;
        q.push({x, y});
      }
    }
  }
  return res == INT_MAX ? -1 : res;
}

int main() {

  int maze[5][5] = {{0, 0, 0, 0, 0},
                    {1, 1, 0, 0, 1},
                    {0, 0, 0, 0, 0},
                    {0, 1, 0, 0, 1},
                    {0, 1, 0, 0, 0}};
  int start[2] = {0, 4};
  int destination[2] = {4, 4};
  cout << findShortestWay(maze, start, destination) << endl;

  return 0;
}
