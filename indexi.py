n = float(input("Enter the amount of the study benefits: "))

index = n * 0.0117
n_after = n + index

print("If the index raise is 1.17 percent, the study benefit,")
print("after a raise, would be", n_after, "euros")

new = n_after * 0.0117
n_new = n_after + new
print("and if there was another index raise, the study\nbenefits would be as much as", n_new, "euros")