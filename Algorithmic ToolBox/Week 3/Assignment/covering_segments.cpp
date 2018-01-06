#include <algorithm>
#include <iostream>
#include <climits>
#include <vector>

using std::vector;

struct Segment {
  long long start, end;
};

vector<long long> optimal_points(vector<Segment> &segments) {
  vector<long long> start_points;
  vector<long long> end_points;
  vector<long long> points;
  for (size_t i = 0; i < segments.size(); ++i) {
    start_points.push_back(segments[i].start);
    end_points.push_back(segments[i].end);
  }
  for(int i = 0; i < segments.size(); ++i){
    // Find the minimum of index and store it in t
    int t = 0;
    for(int j = 0; j < segments.size(); ++j){
      if (end_points[j] < end_points[t]){
        t = j;
      }
    }
    if (end_points[t] == 1e9){
      break;
    }
    points.push_back(end_points[t]);
    // Find all start_points which are less than equal to end_points[t]
    for(int k = 0; k < start_points.size(); k++){
      if (start_points[k] <= end_points[t]){
        start_points[k] = 1e9;
        end_points[k] = 1e9;

      }
    }
    start_points[t] = 1e9;
    end_points[t] = 1e9;
  }
  return points;
}

int main() {
  int n;
  std::cin >> n;
  vector<Segment> segments(n);
  for (size_t i = 0; i < segments.size(); ++i) {
    std::cin >> segments[i].start >> segments[i].end;
  }
  vector<long long> points = optimal_points(segments);
  std::cout << points.size() << "\n";
  for (size_t i = 0; i < points.size(); ++i) {
    std::cout << points[i] << " ";
  }
}
