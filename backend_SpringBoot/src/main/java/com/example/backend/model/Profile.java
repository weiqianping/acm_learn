package com.example.backend.model;

import jakarta.persistence.*;
import java.time.LocalDate;

@Entity
@Table(name = "profile")
public class Profile {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @OneToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "user_id", nullable = false)
    private User user;

    private String avatar;

    @Column(name = "avatar_url")
    private String avatarUrl;

    private LocalDate birthday;

    private String sex;

    private String cellphone;

    // Getters and Setters ...
}
