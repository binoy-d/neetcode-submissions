class Solution:

    def encode(self, strs: List[str]) -> str:
        empty_marker_2 = b'\xe9\xe0\xe7'.decode('latin-1')
        
        if len(strs) == 0:
            return empty_marker_2


        marker = b'\xe2\x82\xac'.decode('latin-1')
        return marker.join(strs) 

    def decode(self, s: str) -> List[str]:
        empty_marker_2 = b'\xe9\xe0\xe7'.decode('latin-1')
        if s == empty_marker_2:
            return []
        marker = b'\xe2\x82\xac'.decode('latin-1')
        return s.split(marker)