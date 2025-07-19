class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        """
        Sort the list of folder paths lexicographically, to
        ensures that any subfolders will follow their parent
        folder in the sorted list.
        """

        folder.sort()
        n = len(folder)
        path = folder[0]
        result = []
        
        """
        Then, iterate through the sorted list and keep track
        of the current top-level folder. If the next folder in
        the list is not a subfolder of the current top-level folder,
        it is added to the result list and becomes the new top-level folder.
        """

        for next in folder:
            if not next.startswith(path + '/'):
                path = next
                result.append(next)

        return result
