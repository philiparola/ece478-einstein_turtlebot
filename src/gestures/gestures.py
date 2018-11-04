# main thread psuedocode
	# setup ros subscriptions and publishers
	# main loop
		# get in face 
		# if face in detection zone
			# detect the side
				# enter animation, animation will have waiting built in to block from main loop
			# else
				# enter otherside animation
		# else (if not in detection zone)
			# pass (perhaps wait?)
	# set break condition for main loop
	# return

# animation pseudocode
	# publish default positions
	# publish arm position
		# order the publishes properly, of course
	# wait
	# publish next arm position in sequeence of poses
	# wait aain
	# repeat this until done
	# wait
	# reset to default position
	# return