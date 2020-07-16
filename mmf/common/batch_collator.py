# Copyright (c) Facebook, Inc. and its affiliates.
from mmf.common.sample import SampleList


class BatchCollator:
    def __init__(self, dataset_name, dataset_type):
        self._dataset_name = dataset_name
        self._dataset_type = dataset_type

    def __call__(self, batch):
        # Create and return sample list with proper name
        # and type set if it is already not a sample list
        # (case of batched iterators)
        if (
            len(batch) == 1
            and isinstance(batch, list)
            and isinstance(batch[0], SampleList)
        ):
            sample_list = batch[0]
        elif not isinstance(batch, SampleList):
            sample_list = SampleList(batch)

        sample_list.dataset_name = self._dataset_name
        sample_list.dataset_type = self._dataset_type
        return sample_list
