import torch
import torch.nn as nn
from typing import List


class Solution:

    def detect_dead_neurons(self, model: nn.Module, x: torch.Tensor) -> List[float]:
        dead_fractions = []
        with torch.no_grad(): # unneeded since only doing forward pass
            for module in model.children():
                x = module(x)
                if isinstance(module, nn.ReLU):
                    dead = (x == 0).all(dim=0).float().mean().item()
                    dead_fractions.append(round(dead, 4))
        return dead_fractions


    def suggest_fix(self, dead_fractions: List[float]) -> str:
        for fraction in dead_fractions:
            if fraction > 0.5:
                return 'use_leaky_relu'
        if dead_fractions[0] > 0.3:
            return 'reinitialize'
        strictly_increasing = True
        for i in range(1, len(dead_fractions)):
            if dead_fractions[i] <= dead_fractions[i - 1]:
                strictly_increasing = False
        if strictly_increasing and dead_fractions[-1] > 0.1:
            return 'reduce_learning_rate'
        if max(dead_fractions) < 0.1:
            return 'healthy'
        return 'healthy'
        # unclean but functional
