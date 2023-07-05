# Planar PIV Standard Name Table

| Standard Name |     units     | Description |
|---------------|:-------------:|:------------|
| final_interrogation_window_size | pixel | Size of the final PIV interogation window. |
| image_particle_density | 1/pixel | Number of particle images per pixel. Equals the number of particles divided by the image area. |
| image_particle_diameter | pixel | The diameter of an image particle. |
| inplane_velocity | m/s | Velocity is a vector quantity. Without a prefix "x", "y" or "z" it indicates the magnitute of the velocity vector. "inplane" indicates that the velocity magnitude was computed based on the in-plane components only. |
| laser_sheet_thickness | m | The width of the laser beam illuminating the seeding particles. |
| mean_image_particle_diameter | pixel | The mean particle diameter in the field of interest. |
| number_of_particles |  | Number of seeding particles in the image or field of interest. |
| piv_mean_seeding_particle_size | um | The mean diameter of the seeding particles. |
| piv_recording | count | The raw unprocessed PIV image as recorded by the used camera. |
| piv_seeding_material |  | The type of particles used for seeding the flow, e.g. Di-ethyl-hexyl-sebacate (DEHS). |
| pulse_delay | s | Time between two laser pulses. |
| saturated_pixel_number |  | Number of pixels in the field of interest that exceed the maximal senor count. |
| standard_deviation_of_image_particle_diameter | pixel | The standard deviation of the image particle diameter in the field of interest. |
| time | s | Recording time since start of recording. |
| velocity | m/s | Velocity is a vector quantity. Without a prefix "x", "y" or "z" it indicates the magnitute of the velocity vector. The magnitude is computed based on all velocity components. |
| x_coordinate | m | Coordinate in x axis direction. |
| x_moving_frame_velocity | m/s | Moving frame velocity is a vector quantity. X indicates the component in x-axis direction. This component is an in-plane component. The velocity depicts the velocity of the moving frame relative to the stationary frame. |
| x_pixel_coordinate | pixel | Image coordinate in horizontal direction. |
| x_pixel_origin | pixel | The pixel x (horizontal) location of the origin used for PIV evaluation |
| x_velocity | m/s | Velocity is a vector quantity. X indicates the component in x-axis direction. This component is an in-plane component. |
| y_coordinate | m | Coordinate in y axis direction. |
| y_moving_frame_velocity | m/s | Moving frame velocity is a vector quantity. Y indicates the component in y-axis direction. This component is an in-plane component. The velocity depicts the velocity of the moving frame relative to the stationary frame. |
| y_pixel_coordinate | pixel | Image coordinate in vertical direction. |
| y_pixel_origin | pixel | The pixel y (vertical) location of the origin used for PIV evaluation |
| y_velocity | m/s | Velocity is a vector quantity. Y indicates the component in y-axis direction. This component is an in-plane component. |
| z_coordinate | m | Coordinate in z axis direction. |
| z_mean_velocity | m/s | Velocity is a vector quantity. Z indicates the component in z-axis direction. Mean indicates that the average over all timesteps was taken. This component is an in-plane component. |
| z_velocity | m/s | Velocity is a vector quantity. Z indicates the component in z-axis direction. This component is the out-of-plane component. |
