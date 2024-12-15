from coding_exercise.domain.model.cable import Cable


class Splitter:

    def __validate(self, len_cable:int, times:int) -> bool:
        """
        """
        # constraints check
        if len_cable >=2 and len_cable <=1024 and times >=1 and times <=64:
            # condition check
            if len_cable > times:
                return True
            else:
                raise ValueError
        else:
            raise ValueError

    def _set_cable_name(self, index:int, cable_name:str) -> str:
        if index > 9:
            return cable_name + "-" + str(index)
        else:
            return cable_name + "-0" + str(index)

    def split(self, cable: Cable, times: int) -> list[Cable]:
        self.__validate(cable.length, times)
        max_split_len = cable.length//(times+1)

        remaining_cable = cable.length
        results = []
        i=0
        while remaining_cable > 0:
            if remaining_cable >= max_split_len:
                results.append(Cable(length=max_split_len, name=self._set_cable_name(i, cable.name)))
                remaining_cable -= max_split_len
            else:
                results.append(Cable(length=remaining_cable, name=self._set_cable_name(i, cable.name)))
                remaining_cable = 0
                break
            i+=1
        return results
